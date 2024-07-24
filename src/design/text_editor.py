# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'text_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFontComboBox, QFrame,
    QGridLayout, QHBoxLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 378)
        MainWindow.setMinimumSize(QSize(620, 260))
        MainWindow.setMaximumSize(QSize(920, 620))
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        # self.actionRecent = QAction(MainWindow)
        # self.actionRecent.setObjectName(u"actionRecent")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(u"actionRename")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionFind_2 = QAction(MainWindow)
        self.actionFind_2.setObjectName(u"actionFind_2")
        self.actionFind_and_Replace = QAction(MainWindow)
        self.actionFind_and_Replace.setObjectName(u"actionFind_and_Replace")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"QFrame {\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(84, 84, 84);\n"
"	border: 0;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(244, 244, 244);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QPushButton::checked {\n"
"	color: rgb(10, 75, 230);\n"
"}\n"
"\n"
"QWidget#widget_color_picker {\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#widget_color {\n"
"	border-radius: 3px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_tools = QFrame(self.central_widget)
        self.frame_tools.setObjectName(u"frame_tools")
        self.frame_tools.setMinimumSize(QSize(0, 30))
        self.frame_tools.setStyleSheet(u"#frame_tools {\n"
"	background-color: rgb(244, 244, 244);\n"
"}")
        self.frame_tools.setFrameShape(QFrame.StyledPanel)
        self.frame_tools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_tools)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 10, 5)
        self.combo_box_fonts = QFontComboBox(self.frame_tools)
        self.combo_box_fonts.setObjectName(u"combo_box_fonts")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.combo_box_fonts.setFont(font)
        self.combo_box_fonts.setStyleSheet(u"QFontComboBox {\n"
"	color: rgb(84, 84, 84);\n"
"	background-color: rgb(244, 244, 244);\n"
"	border-radius: 5px;	\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"}\n"
"\n"
"QFontComboBox::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QFontComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}")
        self.combo_box_fonts.setEditable(False)
        self.combo_box_fonts.setMaxVisibleItems(5)

        self.horizontalLayout_3.addWidget(self.combo_box_fonts)

        self.spin_box_size = QSpinBox(self.frame_tools)
        self.spin_box_size.setObjectName(u"spin_box_size")
        font1 = QFont()
        font1.setPointSize(12)
        self.spin_box_size.setFont(font1)
        self.spin_box_size.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(84, 84, 84);\n"
"	padding-right: 5px;\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(244, 244, 244);\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	subcontrol-origin: border;\n"
"	border: 0;\n"
"	width: 20px;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	subcontrol-origin: border;\n"
"	border: 0;\n"
"	width: 20px;\n"
"}\n"
"")
        self.spin_box_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.spin_box_size)

        self.widget_color_picker = QWidget(self.frame_tools)
        self.widget_color_picker.setObjectName(u"widget_color_picker")
        self.widget_color_picker.setMinimumSize(QSize(20, 20))
        self.widget_color_picker.setMaximumSize(QSize(20, 20))
        self.widget_color_picker.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.widget_color_picker)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.widget_color = QWidget(self.widget_color_picker)
        self.widget_color.setObjectName(u"widget_color")
        self.widget_color.setMinimumSize(QSize(12, 12))
        self.widget_color.setMaximumSize(QSize(12, 12))
        self.widget_color.setStyleSheet(u"background-color: black;")

        self.gridLayout.addWidget(self.widget_color, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget_color_picker)

        self.frame_text = QFrame(self.frame_tools)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setMinimumSize(QSize(70, 0))
        self.frame_text.setMaximumSize(QSize(70, 16777215))
        self.frame_text.setStyleSheet(u"")
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_text)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_bold = QPushButton(self.frame_text)
        self.button_bold.setObjectName(u"button_bold")
        self.button_bold.setMinimumSize(QSize(20, 20))
        self.button_bold.setMaximumSize(QSize(20, 20))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.button_bold.setFont(font2)
        self.button_bold.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_bold)

        self.button_italic = QPushButton(self.frame_text)
        self.button_italic.setObjectName(u"button_italic")
        self.button_italic.setMinimumSize(QSize(20, 20))
        self.button_italic.setMaximumSize(QSize(20, 20))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setItalic(True)
        self.button_italic.setFont(font3)
        self.button_italic.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_italic)

        self.button_underline = QPushButton(self.frame_text)
        self.button_underline.setObjectName(u"button_underline")
        self.button_underline.setMinimumSize(QSize(20, 20))
        self.button_underline.setMaximumSize(QSize(20, 20))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setUnderline(True)
        font4.setStrikeOut(False)
        self.button_underline.setFont(font4)
        self.button_underline.setCheckable(True)

        self.horizontalLayout.addWidget(self.button_underline)


        self.horizontalLayout_3.addWidget(self.frame_text)

        self.frame_align = QFrame(self.frame_tools)
        self.frame_align.setObjectName(u"frame_align")
        self.frame_align.setStyleSheet(u"QPushButton::checked {\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.frame_align.setFrameShape(QFrame.StyledPanel)
        self.frame_align.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_align)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_left = QPushButton(self.frame_align)
        self.button_group_align = QButtonGroup(MainWindow)
        self.button_group_align.setObjectName(u"button_group_align")
        self.button_group_align.addButton(self.button_left)
        self.button_left.setObjectName(u"button_left")
        self.button_left.setMinimumSize(QSize(20, 20))
        self.button_left.setMaximumSize(QSize(20, 20))
        font5 = QFont()
        font5.setBold(True)
        self.button_left.setFont(font5)
        self.button_left.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_left)

        self.button_center = QPushButton(self.frame_align)
        self.button_group_align.addButton(self.button_center)
        self.button_center.setObjectName(u"button_center")
        self.button_center.setMinimumSize(QSize(20, 20))
        self.button_center.setMaximumSize(QSize(20, 20))
        self.button_center.setFont(font5)
        self.button_center.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_center)

        self.button_right = QPushButton(self.frame_align)
        self.button_group_align.addButton(self.button_right)
        self.button_right.setObjectName(u"button_right")
        self.button_right.setMinimumSize(QSize(20, 20))
        self.button_right.setMaximumSize(QSize(20, 20))
        self.button_right.setFont(font5)
        self.button_right.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_right)

        self.button_justify = QPushButton(self.frame_align)
        self.button_group_align.addButton(self.button_justify)
        self.button_justify.setObjectName(u"button_justify")
        self.button_justify.setMinimumSize(QSize(20, 20))
        self.button_justify.setMaximumSize(QSize(20, 20))
        self.button_justify.setFont(font5)
        self.button_justify.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.button_justify)


        self.horizontalLayout_3.addWidget(self.frame_align)

        self.button_spacing = QPushButton(self.frame_tools)
        self.button_spacing.setObjectName(u"button_spacing")
        self.button_spacing.setMinimumSize(QSize(20, 20))
        self.button_spacing.setMaximumSize(QSize(20, 20))
        self.button_spacing.setStyleSheet(u"QPushButton::checked {\n"
"	background-color: rgb(234, 234, 234);\n"
"}")

        self.horizontalLayout_3.addWidget(self.button_spacing)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.frame_tools)

        self.textEdit = QTextEdit(self.central_widget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 770, 24))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuFind = QMenu(self.menuEdit)
        self.menuFind.setObjectName(u"menuFind")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuWindow = QMenu(self.menubar)
        self.menuWindow.setObjectName(u"menuWindow")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuRecent = QMenu(self.menubar)
        self.menuRecent.setObjectName(u"menuRecent")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuFind.menuAction())
        self.menuFind.addAction(self.actionFind_2)
        self.menuFind.addAction(self.actionFind_and_Replace)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R&R Text Editor", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionRename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionFind_2.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.actionFind_and_Replace.setText(QCoreApplication.translate("MainWindow", u"Find and Replace", None))
#if QT_CONFIG(tooltip)
        self.combo_box_fonts.setToolTip(QCoreApplication.translate("MainWindow", u"Font", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spin_box_size.setToolTip(QCoreApplication.translate("MainWindow", u"Text Size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.button_bold.setToolTip(QCoreApplication.translate("MainWindow", u"Bold", None))
#endif // QT_CONFIG(tooltip)
        self.button_bold.setText(QCoreApplication.translate("MainWindow", u"B", None))
#if QT_CONFIG(tooltip)
        self.button_italic.setToolTip(QCoreApplication.translate("MainWindow", u"Italic", None))
#endif // QT_CONFIG(tooltip)
        self.button_italic.setText(QCoreApplication.translate("MainWindow", u"I", None))
#if QT_CONFIG(tooltip)
        self.button_underline.setToolTip(QCoreApplication.translate("MainWindow", u"Underline", None))
#endif // QT_CONFIG(tooltip)
        self.button_underline.setText(QCoreApplication.translate("MainWindow", u"U", None))
#if QT_CONFIG(tooltip)
        self.button_left.setToolTip(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(tooltip)
        self.button_left.setText("")
#if QT_CONFIG(tooltip)
        self.button_center.setToolTip(QCoreApplication.translate("MainWindow", u"Center", None))
#endif // QT_CONFIG(tooltip)
        self.button_center.setText("")
#if QT_CONFIG(tooltip)
        self.button_right.setToolTip(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(tooltip)
        self.button_right.setText("")
#if QT_CONFIG(tooltip)
        self.button_justify.setToolTip(QCoreApplication.translate("MainWindow", u"Justify", None))
#endif // QT_CONFIG(tooltip)
        self.button_justify.setText("")
#if QT_CONFIG(tooltip)
        self.button_spacing.setToolTip(QCoreApplication.translate("MainWindow", u"Spacing", None))
#endif // QT_CONFIG(tooltip)
        self.button_spacing.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuFind.setTitle(QCoreApplication.translate("MainWindow", u"Find", None))
        self.menuRecent.setTitle(QCoreApplication.translate("MainWindow", u"Recent", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuWindow.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

