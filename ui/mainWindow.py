# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from resources import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(321, 404)
        icon = QIcon()
        icon.addFile(u":/icons/icons/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 301, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listWidget.setProperty("showDropIndicator", False)
        self.listWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.listWidget)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 16))
        self.currentSkinLabel = QLabel(self.centralwidget)
        self.currentSkinLabel.setObjectName(u"currentSkinLabel")
        self.currentSkinLabel.setGeometry(QRect(100, 10, 211, 16))
        self.apply = QPushButton(self.centralwidget)
        self.apply.setObjectName(u"apply")
        self.apply.setGeometry(QRect(170, 350, 141, 23))
        self.gameRoot = QPushButton(self.centralwidget)
        self.gameRoot.setObjectName(u"gameRoot")
        self.gameRoot.setGeometry(QRect(10, 350, 131, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 321, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuStyles = QMenu(self.menubar)
        self.menuStyles.setObjectName(u"menuStyles")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuStyles.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuStyles.addAction(self.actionLight)
        self.menuStyles.addAction(self.actionDark)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yandere Sim Skin Switcher", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Skin Mod: ", None))
        self.currentSkinLabel.setText("")
        self.apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.gameRoot.setText(QCoreApplication.translate("MainWindow", u"Yandere Game Root", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuStyles.setTitle(QCoreApplication.translate("MainWindow", u"Styles", None))
    # retranslateUi

