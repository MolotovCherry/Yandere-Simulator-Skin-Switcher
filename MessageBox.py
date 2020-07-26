from PySide2.QtCore import QTimer, Qt
from PySide2.QtWidgets import QDialog, QLayout

from qtmodern.windows import ModernWindow
from ui.messageBox import Ui_MessageBox


class MessageBox(QDialog):
    def __init__(self, icon=None, title=None, text=None, detailedText=None, parent=None):
        super().__init__(parent)

        self.ui = Ui_MessageBox()
        self.ui.setupUi(self)

        # hide detail elements
        self.ui.line.hide()
        self.ui.errorDetails.hide()
        self.ui.showDetailsBtn.clicked.connect(self.showDetails)
        self.ui.okBtn.clicked.connect(self.close)

        self.timer = QTimer()

        self.detailsShown = False

        if icon:
            # requires QStyle.SP_MessageBox type of icon
            self.setIcon(icon)
        if title:
            self.setWindowTitle(title)
        if text:
            self.setText(text)
        if detailedText:
            self.detailsEnabled = True
            self.setDetailedText(detailedText)
        else:
            self.detailsEnabled = False

        self.setShowDetailsEnabled(self.detailsEnabled)

        self.mw = ModernWindow(self)
        self.mw.btnMinimize.setEnabled(False)
        self.mw.btnMinimize.setVisible(False)
        self.mw.btnMaximize.setVisible(False)
        self.mw.btnRestore.setVisible(False)
        self.setupEvents()

    def show(self):
        super().show()
        self.mw.show()

    def showEvent(self, event):
        super().showEvent(event)

        # keep button from shrinking
        if self.detailsEnabled:
            self.ui.showDetailsBtn.setMinimumWidth(self.ui.showDetailsBtn.width())

    def close(self):
        super().close()
        self.mw.close()

    def setupEvents(self):
        flags = self.mw.windowFlags()
        flags |= Qt.WindowStaysOnTopHint

        self.mw.setWindowFlags(flags)
        # keep focus on messagebox only
        self.mw.setWindowModality(Qt.ApplicationModal)

        self.mw.layout().setSizeConstraint(QLayout.SetFixedSize)

    def setIcon(self, icon):
        ''' Icon can be any one of these
        QStyle::SP_MessageBoxInformation
        QStyle::SP_MessageBoxWarning
        QStyle::SP_MessageBoxCritical
        QStyle::SP_MessageBoxQuestion
        '''
        icon = self.style().standardIcon(icon).pixmap(96, 96)
        self.ui.boxIcon.setPixmap(icon)

    def setShowDetailsEnabled(self, flag):
        self.detailsEnabled = flag
        if flag:
            self.ui.showDetailsBtn.show()
        else:
            self.ui.showDetailsBtn.hide()
        self.timer.singleShot(0, lambda: self.mw.resize(0, 0))

    def showDetails(self):
        if not self.detailsShown:
            self.ui.line.show()
            self.ui.errorDetails.show()
            self.ui.showDetailsBtn.setText('Hide Details...')
            self.detailsShown = True
            self.timer.singleShot(0, lambda: self.mw.resize(0, 0))
        else:
            self.ui.errorDetails.hide()
            self.ui.line.hide()
            self.ui.showDetailsBtn.setText('Show Details...')
            self.detailsShown = False
            self.timer.singleShot(0, lambda: self.mw.resize(0, 0))

    def setText(self, text):
        self.ui.message.setText(text)

    def setDetailedText(self, text):
        self.ui.errorDetails.setPlainText(text)
