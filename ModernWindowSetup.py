from PySide2.QtWidgets import QStyle, QApplication
from PySide2.QtCore import Qt
import qtmodern.windows


def setup():
    '''
        This patches the ModernWindow variables and methods to be more
        compatible with this app
    '''
    qtmodern.windows.ModernWindow.on_titleBar_doubleClicked = lambda x: None

    __initBac = qtmodern.windows.ModernWindow.__init__
    def __init__(self, w, parent=None):
        __initBac(self, w, parent=None)

        # windows appear in center of screen
        # now I know that __init__ sets geometry already
        # but it's always in the top left corner
        rect = QStyle.alignedRect(
            Qt.LeftToRight, Qt.AlignCenter, w.size(),
            QApplication.instance().desktop().availableGeometry()
        )
        self.setGeometry(rect)

        self.btnRestore.setEnabled(False)
        self.btnMaximize.setEnabled(False)

        flags = self.windowFlags() | Qt.MSWindowsFixedSizeDialogHint
        self.setWindowFlags(flags)

        self.setAttribute(Qt.WA_DeleteOnClose, True)

    qtmodern.windows.ModernWindow.__init__ = __init__
