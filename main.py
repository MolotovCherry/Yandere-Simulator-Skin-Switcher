import ctypes
import sys
import logging
import os
import shutil
from traceback import format_exception
from types import MethodType as instancemethod

import ModernWindowSetup
import qtmodern.styles
from qtmodern.windows import ModernWindow
from Configuration import Configuration
from MessageBox import MessageBox
from ui.mainWindow import Ui_MainWindow

from PySide2.QtCore import QMetaObject, Qt, Signal
from PySide2.QtWidgets import QApplication, QStyle, QMainWindow, QFileDialog, QListWidgetItem, QListWidget
from PySide2.QtWinExtras import QWinTaskbarButton


# set up the modern window patches
ModernWindowSetup.setup()

# logger stuff
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s: %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)

# we do this to allow the windows taskbar icon to show
myappid = 'private.yanderesimskinswitcher.10'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

def displayException(etype, value, tb):
    messageRaw = format_exception(etype, value, tb)
    message = '\n'.join(messageRaw)
    mbox = MessageBox(QStyle.SP_MessageBoxCritical, 'Critical Exception', messageRaw[(-1)], message)
    logger.fatal(message)
    mbox.show()
    mbox.exec_()

    # this keeps cx_freeze from displaying a traceback when program fails
    # not a direct call since errors can occur before the event loop starts
    # and QApplication.quit() is a no-op before the event loop starts, so we
    # must let this event process once it starts in order to make it actually quit
    QMetaObject.invokeMethod(QApplication.instance(), 'quit', Qt.QueuedConnection)
sys.excepthook = displayException

# for listWidget's deselection clicking, override
def mousePressEvent(self, event):
    self.clearSelection()
    self.clearFocus()
    QListWidget.mousePressEvent(self, event)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName('MainWindow')

        # set up UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # get the configuration object
        self.config: Configuration = Configuration()

        # cached for the style selecting
        self.app: QApplication = QApplication.instance()

        # window can't be resized
        self.setFixedSize(self.geometry().width(), self.geometry().height())

        self.ui.actionExit.triggered.connect(self.menuExit)
        self.ui.actionLight.triggered.connect(lambda: self.setStyle('light'))
        self.ui.actionDark.triggered.connect(lambda: self.setStyle('dark'))

        # set the style menu actions enabled or disabled based upon current theme
        self.style: str = self.config['default'].get('style', 'dark')
        if self.style == 'light':
            self.ui.actionLight.setEnabled(False)
        elif self.style == 'dark':
            self.ui.actionDark.setEnabled(False)
        
        self.needBrowse = True
        self.gameRoot = self.config['default'].get('gameroot', '')
        if self.gameRoot != '':
            self.needBrowse = False
            self.gameRoot = os.path.join(self.gameRoot, 'YandereSimulator_Data/StreamingAssets')

        self.currentSkin = self.config['default'].get('currentskin', 'default')
        self.ui.currentSkinLabel.setText(self.currentSkin)

        self.ui.apply.clicked.connect(self.apply)
        self.ui.gameRoot.clicked.connect(self.browseDirectory)

        # exe or not?
        if hasattr(sys, 'frozen'):
            path = os.path.dirname(os.path.abspath(sys.executable))
        else:
            path = os.path.dirname(os.path.realpath(__file__))
        self.skinDir = os.path.join(path, 'skins')

        # populate mod list
        _, dirs, _ = next(os.walk(self.skinDir))
        for dir in dirs:
            item = QListWidgetItem(dir)
            self.ui.listWidget.addItem(item)

        self.ui.listWidget.currentItemChanged.connect(self.changeSelection)
        # replace mousePress to get deselection clicking
        self.ui.listWidget.mousePressEvent = instancemethod(mousePressEvent, self.ui.listWidget)

        self.defaultFiles = (
            'CustomUniform.png',
            'CustomLong.png',
            'CustomSweater.png',
            'CustomBlazer.png',
            'CustomArms.png',
            'CustomFace.png',
            'CustomSwimsuit.png',
            'CustomGym.png',
            'CustomNude.png',
            'CustomHair.png',
            'CustomDrills.png',
            'CustomLongHairA.png',
            'CustomLongHairB.png',
            'CustomLongHairC.png',
            'CustomStockings1.png',
            'CustomStockings2.png',
            'CustomStockings3.png',
            'CustomStockings4.png',
            'CustomStockings5.png',
            'CustomStockings6.png',
            'CustomStockings7.png',
            'CustomStockings8.png',
            'CustomStockings9.png',
            'CustomStockings10.png'
            # CustomPortrait is a special case
        )

        # create the modernwindow instance
        self.mw = ModernWindow(self, self)

    def browseDirectory(self, _):
        self.gameRoot = str(QFileDialog.getExistingDirectory(self, 'Select Yandere Game Root Directory'))
        if self.gameRoot != '':
            self.config.set('default', 'gameroot', self.gameRoot)
            self.needBrowse = False
            self.gameRoot = os.path.join(self.gameRoot, 'YandereSimulator_Data/StreamingAssets')
        else:
            self.needBrowse = True

    def apply(self, _):
        if self.needBrowse:
            self.gameRoot = str(QFileDialog.getExistingDirectory(self, 'Select Yandere Game Root Directory'))
            if self.gameRoot != '':
                self.config.set('default', 'gameroot', self.gameRoot)
                self.needBrowse = False
                self.gameRoot = os.path.join(self.gameRoot, 'YandereSimulator_Data/StreamingAssets')
            else:
                self.needBrowse = True
            
        if not self.needBrowse:
            if len(self.ui.listWidget.selectedItems()) > 0:
                skin = self.ui.listWidget.selectedItems()[0].text()
                self.ui.currentSkinLabel.setText(skin)
                self.config.set('default', 'currentskin', skin)
                
                if (skin == 'default') and (self.currentSkin != 'default'):
                    # delete skin files
                    self.setDefaultSkin()
                    self.copyDefaultSkinFiles()

                    mbox = MessageBox(QStyle.SP_MessageBoxInformation, 'Successfully Applied', 'Applied new mod skin:\ndefault')
                    mbox.show()
                    mbox.exec_()

                    self.ui.apply.setEnabled(False)
                    print('Applied ' + skin)
                elif skin != self.currentSkin:
                    # we need to wipe any previous skin files first
                    # in order to make sure the new skin is freshly applied
                    self.setDefaultSkin()
                
                    portrait = False
                    _, _, files = next(os.walk(os.path.join(self.skinDir, skin)))
                    for file in files:
                        if (file in self.defaultFiles) or (file == 'CustomPortrait.png'):
                            shutil.copy2(os.path.join(os.path.join(self.skinDir, skin), file), self.gameRoot)
                            print('Added ' + file)
                            if file == 'CustomPortrait.png':
                                portrait = True
                                self.setPortrait(True)
                    
                    if not portrait:
                        self.setPortrait(False)
                
                    print('Applied ' + skin)
                    self.ui.apply.setEnabled(False)
                    
                    mbox = MessageBox(QStyle.SP_MessageBoxInformation, 'Successfully Applied', 'Applied new mod skin:\n' + skin)
                    mbox.show()
                    mbox.exec_()

                self.currentSkin = skin

    def changeSelection(self, current, _):
        if current.text() == self.currentSkin:
            self.ui.apply.setEnabled(False)
        else:
            self.ui.apply.setEnabled(True)

    def setPortrait(self, enabled):
        checkFor = '0' if enabled else '1'
        writeVal = '1' if enabled else '0'
        # handle the portrait
        with open(os.path.join(self.gameRoot, 'CustomPortrait.txt'), 'r+') as f:
            t = f.read()
            if t == checkFor:
                f.seek(0)
                f.truncate(0)
                f.write(writeVal)

    def copyDefaultSkinFiles(self):
        _, _, files = next(os.walk(os.path.join(self.skinDir, 'default')))
        for file in files:
            # this will cause it to skip CustomPortrait.png if it was not removed
            if not os.path.exists(os.path.join(self.gameRoot, file)):
                print('Added ' + file)
                shutil.copy2(os.path.join(os.path.join(self.skinDir, 'default'), file), self.gameRoot)

    def setDefaultSkin(self):
        _, _, files = next(os.walk(self.gameRoot))
        for file in files:
            if file in self.defaultFiles:
                print('Removed ' + file)
                os.remove(os.path.join(self.gameRoot, file))
                
        # handle the portrait
        with open(os.path.join(self.gameRoot, 'CustomPortrait.txt'), 'r+') as f:
            t = f.read()
            if t == '1':
                os.remove(os.path.join(self.gameRoot, 'CustomPortrait.png'))
                print('Removed CustomPortrait.png')
                f.seek(0)
                f.truncate(0)
                f.write('0')
                

    def closeEvent(self, event):
        # save config before closing
        self.config.saveConfig()

    def show(self):
        super().show()
        # this simplifies the process of MW
        # one show event for our mainwindow sets up MW too
        self.mw.show()

    def setStyle(self, style: str):
        if style == 'light':
            qtmodern.styles.light(self.app)
            self.ui.actionLight.setEnabled(False)
            self.ui.actionDark.setEnabled(True)
            self.config.set('default', 'style', 'light')
        elif style == 'dark':
            qtmodern.styles.dark(self.app)
            self.ui.actionLight.setEnabled(True)
            self.ui.actionDark.setEnabled(False)
            self.config.set('default', 'style', 'dark')

    def menuExit(self):
        # save config before closing
        self.config.saveConfig()
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps)

    config = Configuration()

    # set the application style
    style = config['default'].get('style', 'light')
    if style == 'light':
        qtmodern.styles.light(app)
    elif style == 'dark':
        qtmodern.styles.dark(app)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())