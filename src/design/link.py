# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'link.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_DialogPasteLink(object):
    def setupUi(self, DialogPasteLink):
        if not DialogPasteLink.objectName():
            DialogPasteLink.setObjectName(u"DialogPasteLink")
        DialogPasteLink.resize(360, 130)
        DialogPasteLink.setMinimumSize(QSize(0, 130))
        DialogPasteLink.setMaximumSize(QSize(16777215, 130))
        DialogPasteLink.setStyleSheet(u"QDialog {\n"
"	background-color: white;\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 1px solid rgb(224, 224, 224);\n"
"	border-radius: 4px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton#button_ok {\n"
"	color: white;\n"
"	background-color: rgb(25, 110, 255);\n"
"}\n"
"\n"
"QPushButton::pressed#button_ok {\n"
"	background-color: rgb(10, 85, 230);\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
"}")
        self.verticalLayout = QVBoxLayout(DialogPasteLink)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.label = QLabel(DialogPasteLink)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 11))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(DialogPasteLink)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 45))
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.lineEdit)

        self.frame_8 = QFrame(DialogPasteLink)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 20))
        self.frame_8.setMaximumSize(QSize(16777215, 25))
        self.frame_8.setMouseTracking(False)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_7 = QSpacerItem(187, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.button_cancel = QPushButton(self.frame_8)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMinimumSize(QSize(70, 18))
        self.button_cancel.setMaximumSize(QSize(70, 18))
        self.button_cancel.setFont(font)

        self.horizontalLayout_7.addWidget(self.button_cancel)

        self.button_ok = QPushButton(self.frame_8)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setMinimumSize(QSize(70, 18))
        self.button_ok.setMaximumSize(QSize(70, 18))
        self.button_ok.setFont(font)

        self.horizontalLayout_7.addWidget(self.button_ok)


        self.verticalLayout.addWidget(self.frame_8)


        self.retranslateUi(DialogPasteLink)

        QMetaObject.connectSlotsByName(DialogPasteLink)
    # setupUi

    def retranslateUi(self, DialogPasteLink):
        DialogPasteLink.setWindowTitle(QCoreApplication.translate("DialogPasteLink", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogPasteLink", u"Web-adress:", None))
        self.button_cancel.setText(QCoreApplication.translate("DialogPasteLink", u"Cancel", None))
        self.button_ok.setText(QCoreApplication.translate("DialogPasteLink", u"OK", None))
    # retranslateUi

