# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'messageBox.ui'
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

class Ui_MessageBox(object):
    def setupUi(self, MessageBox):
        if not MessageBox.objectName():
            MessageBox.setObjectName(u"MessageBox")
        MessageBox.resize(290, 177)
        MessageBox.setMinimumSize(QSize(290, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons/app.ico", QSize(), QIcon.Normal, QIcon.Off)
        MessageBox.setWindowIcon(icon)
        MessageBox.setModal(True)
        self.verticalLayout = QVBoxLayout(MessageBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.boxIcon = QLabel(MessageBox)
        self.boxIcon.setObjectName(u"boxIcon")
        self.boxIcon.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.boxIcon)

        self.horizontalSpacer_2 = QSpacerItem(15, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.message = QLabel(MessageBox)
        self.message.setObjectName(u"message")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setScaledContents(True)
        self.message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.message.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.message)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okBtn = QPushButton(MessageBox)
        self.okBtn.setObjectName(u"okBtn")

        self.horizontalLayout.addWidget(self.okBtn)

        self.showDetailsBtn = QPushButton(MessageBox)
        self.showDetailsBtn.setObjectName(u"showDetailsBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.showDetailsBtn.sizePolicy().hasHeightForWidth())
        self.showDetailsBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.showDetailsBtn)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.line = QFrame(MessageBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.errorDetails = QPlainTextEdit(MessageBox)
        self.errorDetails.setObjectName(u"errorDetails")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.errorDetails.sizePolicy().hasHeightForWidth())
        self.errorDetails.setSizePolicy(sizePolicy2)
        self.errorDetails.setMinimumSize(QSize(0, 100))
        self.errorDetails.setAcceptDrops(False)
        self.errorDetails.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.errorDetails.setDocumentTitle(u"")
        self.errorDetails.setUndoRedoEnabled(False)
        self.errorDetails.setReadOnly(True)
        self.errorDetails.setPlainText(u"")

        self.verticalLayout.addWidget(self.errorDetails)


        self.retranslateUi(MessageBox)

        QMetaObject.connectSlotsByName(MessageBox)
    # setupUi

    def retranslateUi(self, MessageBox):
        MessageBox.setWindowTitle(QCoreApplication.translate("MessageBox", u"Title", None))
        self.boxIcon.setText("")
        self.message.setText(QCoreApplication.translate("MessageBox", u"Text", None))
        self.okBtn.setText(QCoreApplication.translate("MessageBox", u"Ok", None))
        self.showDetailsBtn.setText(QCoreApplication.translate("MessageBox", u"Show Details...", None))
    # retranslateUi

