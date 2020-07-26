from os.path import join, dirname, abspath

from PySide2.QtGui import QGuiApplication
from qtpy.QtCore import Qt, QMetaObject, Signal, Slot, QFile, QIODevice, QTextStream, QEvent
from qtpy.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QToolButton,
                            QLabel, QSizePolicy, QApplication, QDockWidget, QStyle, QSpacerItem)

from ._utils import QT_VERSION

from . import globals


class WindowDragger(QWidget):
    """ Window dragger.

        Args:
            window (QWidget): Associated window.
            parent (QWidget, optional): Parent widget.
    """

    doubleClicked = Signal()

    def __init__(self, window, parent=None):
        super().__init__(parent)

        self._window = window
        self._mousePressed = False

    def mousePressEvent(self, event):
        self._mousePressed = True
        self._mousePos = event.globalPos()
        self._windowPos = self._window.pos()
        self._sizeW = self._window.width()
        self._sizeH = self._window.height()
        screen = QGuiApplication.primaryScreen()
        screenRect = screen.geometry()
        self._screenSizeW = screenRect.width()
        self._screenSizeH = screenRect.height()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            coords = self._windowPos + (event.globalPos() - self._mousePos)
            # enforce that window never goes beyond borders
            if (((coords.x() + self._sizeW <= self._screenSizeW) and
                 (coords.y() + self._sizeH <= self._screenSizeH)) and
                    ((coords.x() >= 0) and
                     (coords.y() >= 0))):

                self._window.move(coords)

    def mouseReleaseEvent(self, event):
        self._mousePressed = False

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()


class ModernWindow(QWidget):
    """ Modern window.

        Args:
            w (QWidget): Main widget.
            parent (QWidget, optional): Parent widget.
    """

    windowCollapse = Signal()
    windowUncollapse = Signal()
    minimized = Signal()
    unMinimized = Signal()

    def __init__(self, w, parent=None):
        super().__init__(parent)

        self.setupUi()
        self.setupEvents(w)

        contentLayout = QHBoxLayout()
        contentLayout.setContentsMargins(0, 0, 0, 0)
        contentLayout.addWidget(w)

        self.windowContent.setLayout(contentLayout)

        self.setWindowTitle(w.windowTitle())
        self.setGeometry(w.geometry())

    def setupUi(self):
        # create title bar, content
        self.vboxWindow = QVBoxLayout(self)
        self.vboxWindow.setContentsMargins(0, 0, 0, 0)

        self.windowFrame = QWidget(self)
        self.windowFrame.setObjectName('windowFrame')

        self.vboxFrame = QVBoxLayout(self.windowFrame)
        self.vboxFrame.setContentsMargins(0, 0, 0, 0)

        self.titleBar = WindowDragger(self, self.windowFrame)
        self.titleBar.setObjectName('titleBar')
        self.titleBar.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                QSizePolicy.Fixed))

        self.hboxTitle = QHBoxLayout(self.titleBar)
        self.hboxTitle.setContentsMargins(0, 0, 0, 0)
        self.hboxTitle.setSpacing(0)

        self.lblTitle = QLabel('Title')
        self.lblTitle.setObjectName('lblTitle')
        self.lblTitle.setAlignment(Qt.AlignCenter)
        self.hboxTitle.addWidget(self.lblTitle)

        spButtons = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.dragArea = QWidget(self.titleBar)
        self.dragArea.setObjectName('dragArea')
        self.dragAreaLayout = QHBoxLayout(self.dragArea)
        self.spacer = QSpacerItem(20, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.dragArea.setVisible(False)
        self.dragAreaLayout.addItem(self.spacer)
        self.hboxTitle.addWidget(self.dragArea)

        self.btnCollapse = QToolButton(self.titleBar)
        self.btnCollapse.setObjectName('btnCollapse')
        self.btnCollapse.setSizePolicy(spButtons)
        self.btnCollapse.setVisible(False)
        self.hboxTitle.addWidget(self.btnCollapse)

        self.btnUncollapse = QToolButton(self.titleBar)
        self.btnUncollapse.setObjectName('btnUncollapse')
        self.btnUncollapse.setSizePolicy(spButtons)
        self.btnUncollapse.setVisible(False)
        self.hboxTitle.addWidget(self.btnUncollapse)

        self.btnMinimize = QToolButton(self.titleBar)
        self.btnMinimize.setObjectName('btnMinimize')
        self.btnMinimize.setSizePolicy(spButtons)
        self.hboxTitle.addWidget(self.btnMinimize)

        self.btnRestore = QToolButton(self.titleBar)
        self.btnRestore.setObjectName('btnRestore')
        self.btnRestore.setSizePolicy(spButtons)
        self.btnRestore.setVisible(False)
        self.hboxTitle.addWidget(self.btnRestore)

        self.btnMaximize = QToolButton(self.titleBar)
        self.btnMaximize.setObjectName('btnMaximize')
        self.btnMaximize.setSizePolicy(spButtons)
        self.hboxTitle.addWidget(self.btnMaximize)

        self.btnClose = QToolButton(self.titleBar)
        self.btnClose.setObjectName('btnClose')
        self.btnClose.setSizePolicy(spButtons)
        self.hboxTitle.addWidget(self.btnClose)

        self.vboxFrame.addWidget(self.titleBar)

        self.windowContent = QWidget(self.windowFrame)
        self.vboxFrame.addWidget(self.windowContent)

        self.vboxWindow.addWidget(self.windowFrame)

        # set window flags
        self.setWindowFlags(
                Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint)

        if QT_VERSION >= (5,):
            self.setAttribute(Qt.WA_TranslucentBackground)

        self.updateFrameSheet()

        # automatically connect slots
        QMetaObject.connectSlotsByName(self)

    def updateFrameSheet(self):
        if globals.applied_style == 'light':
            f = QFile(':/frameless-light.qss')
        elif globals.applied_style == 'dark':
            f = QFile(':/frameless-dark.qss')
        else:
            raise RuntimeError('Set the app style theme before instantiating ModernWindow')
        f.open(QIODevice.ReadOnly | QIODevice.Text)
        text = QTextStream(f)
        text.setCodec('UTF-8')
        text = text.readAll()

        self.setStyleSheet(text)
        f.close()

    def changeEvent(self, event):
        if event.type() == QEvent.PaletteChange:
            self.updateFrameSheet()
        elif event.type() == QEvent.WindowStateChange:
            if self.windowState() == Qt.WindowMinimized:
                self.minimized.emit()
            elif self.windowState() == Qt.WindowNoState:
                self.unMinimized.emit()

    def setupEvents(self, w):
        self.setWindowIcon(w.windowIcon())
        w.close = self.close
        self.closeEvent = w.closeEvent

    def setWindowTitle(self, title):
        """ Set window title.

            Args:
                title (str): Title.
        """

        super(ModernWindow, self).setWindowTitle(title)
        self.lblTitle.setText(title)

    @Slot()
    def on_btnMinimize_clicked(self):
        self.setWindowState(Qt.WindowMinimized)

    @Slot()
    def on_btnRestore_clicked(self):
        self.btnRestore.setVisible(False)
        self.btnMaximize.setVisible(True)

        self.setWindowState(Qt.WindowNoState)

    @Slot()
    def on_btnMaximize_clicked(self):
        self.btnRestore.setVisible(True)
        self.btnMaximize.setVisible(False)

        self.setWindowState(Qt.WindowMaximized)

    @Slot()
    def on_btnClose_clicked(self):
        self.close()

    @Slot()
    def on_titleBar_doubleClicked(self):
        if self.btnMaximize.isVisible():
            self.on_btnMaximize_clicked()
        else:
            self.on_btnRestore_clicked()

    @Slot()
    def on_btnCollapse_clicked(self):
        self.windowCollapse.emit()

    @Slot()
    def on_btnUncollapse_clicked(self):
        self.windowUncollapse.emit()
