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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QFontComboBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)
from src.rc import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(770, 378)
        MainWindow.setMinimumSize(QSize(620, 260))
        MainWindow.setMaximumSize(QSize(920, 620))
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_close = QAction(MainWindow)
        self.action_close.setObjectName(u"action_close")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_rename = QAction(MainWindow)
        self.action_rename.setObjectName(u"action_rename")
        self.action_cut = QAction(MainWindow)
        self.action_cut.setObjectName(u"action_cut")
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        self.action_paste = QAction(MainWindow)
        self.action_paste.setObjectName(u"action_paste")
        self.action_delete = QAction(MainWindow)
        self.action_delete.setObjectName(u"action_delete")
        self.action_find = QAction(MainWindow)
        self.action_find.setObjectName(u"action_find")
        self.action_find_and_replace = QAction(MainWindow)
        self.action_find_and_replace.setObjectName(u"action_find_and_replace")
        self.action_print = QAction(MainWindow)
        self.action_print.setObjectName(u"action_print")
        self.action_paste_link = QAction(MainWindow)
        self.action_paste_link.setObjectName(u"action_paste_link")
        self.action_bold = QAction(MainWindow)
        self.action_bold.setObjectName(u"action_bold")
        self.action_bold.setCheckable(True)
        self.action_italic = QAction(MainWindow)
        self.action_italic.setObjectName(u"action_italic")
        self.action_italic.setCheckable(True)
        self.action_underline = QAction(MainWindow)
        self.action_underline.setObjectName(u"action_underline")
        self.action_underline.setCheckable(True)
        self.action_left = QAction(MainWindow)
        self.action_left.setObjectName(u"action_left")
        self.action_left.setCheckable(True)
        self.action_center = QAction(MainWindow)
        self.action_center.setObjectName(u"action_center")
        self.action_center.setCheckable(True)
        self.action_right = QAction(MainWindow)
        self.action_right.setObjectName(u"action_right")
        self.action_right.setCheckable(True)
        self.action_justify = QAction(MainWindow)
        self.action_justify.setObjectName(u"action_justify")
        self.action_justify.setCheckable(True)
        self.action_indent = QAction(MainWindow)
        self.action_indent.setObjectName(u"action_indent")
        self.action_unindent = QAction(MainWindow)
        self.action_unindent.setObjectName(u"action_unindent")
        self.action_redo = QAction(MainWindow)
        self.action_redo.setObjectName(u"action_redo")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget.setStyleSheet(u"QToolTip {\n"
"	background-color: rgb(234, 234, 234);\n"
"	color: rgb(84, 84, 84);\n"
"}\n"
"\n"
"QTextEdit {\n"
"	background-color: white;\n"
"}\n"
"\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: rgb(84, 84, 84);\n"
"	border: 0;\n"
"	border-radius: 4px;\n"
"	background-color: rgb(244, 244, 244);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: rgb(84, 84, 84);\n"
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
        self.frame_tools.setMaximumSize(QSize(16777215, 30))
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
"	padding-left: 2px;\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"}\n"
"\n"
"QFontComboBox::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QFontComboBox::drop-down {\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QFontComboBox::down-arrow {\n"
"	subcontrol-position: margin;\n"
"	subcontrol-origin: border;\n"
"	border-image: url(:/icons/icons/arrows.png);\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	border-radius: 4px;\n"
"	margin-top: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	selection-background-color: rgb(70, 140, 255);\n"
"	selection-color: white;\n"
"	background-color: rgb(244, 244, 244);\n"
"	color: rgb(84, 84, 84);\n"
"}\n"
"")
        self.combo_box_fonts.setEditable(False)
        self.combo_box_fonts.setMaxVisibleItems(5)

        self.horizontalLayout_3.addWidget(self.combo_box_fonts)

        self.combo_box_styles = QComboBox(self.frame_tools)
        self.combo_box_styles.setObjectName(u"combo_box_styles")
        font1 = QFont()
        font1.setPointSize(12)
        self.combo_box_styles.setFont(font1)
        self.combo_box_styles.setStyleSheet(u"QComboBox {\n"
"	color: rgb(84, 84, 84);\n"
"	background-color: rgb(244, 244, 244);\n"
"	border-radius: 5px;	\n"
"	padding-left: 2px;\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"}\n"
"\n"
"QComboBox::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	subcontrol-position: margin;\n"
"	subcontrol-origin: border;\n"
"	border-image: url(:/icons/icons/arrows.png);\n"
"	height: 12px;\n"
"	width: 12px;\n"
"	border-radius: 4px;\n"
"	margin-top: 2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	selection-background-color: rgb(70, 140, 255);\n"
"	selection-color: white;\n"
"	background-color: rgb(244, 244, 244);\n"
"	color: rgb(84, 84, 84);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.combo_box_styles)

        self.spin_box_size = QSpinBox(self.frame_tools)
        self.spin_box_size.setObjectName(u"spin_box_size")
        self.spin_box_size.setFont(font1)
        self.spin_box_size.setStyleSheet(u"QSpinBox {\n"
"	color: rgb(84, 84, 84);\n"
"	border: 1px solid rgb(234, 234, 234);\n"
"	border-radius: 5px;\n"
"	background-color: rgb(244, 244, 244);\n"
"	padding-left: 2px;\n"
"}\n"
"\n"
"QSpinBox::hover {\n"
"	background-color: rgb(234, 234, 234);\n"
"}\n"
"\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"	subcontrol-origin: border;\n"
"	margin-right: 5px;\n"
"	width: 9px;\n"
"	height: 8px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"	subcontrol-position: top right;\n"
"	margin-top: 2px;\n"
"	border-image: url(:/icons/icons/arrow_up.png) 1;\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"	subcontrol-position: bottom right;\n"
"	margin-bottom: 3px;\n"
"	border-image: url(:/icons/icons/arrow_down.png) 1;\n"
"}\n"
"\n"
"QSpinBox::up-button::hover,  QSpinBox::down-button::hover {\n"
"	background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QSpinBox::up-button::pressed, QSpinBox::down-button::pressed  {\n"
"	background-color: rgb(214, 214, 214);\n"
"}\n"
"\n"
"\n"
"")
        self.spin_box_size.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.spin_box_size.setMinimum(1)
        self.spin_box_size.setMaximum(288)

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

        self.frame_find_and_replace = QFrame(self.central_widget)
        self.frame_find_and_replace.setObjectName(u"frame_find_and_replace")
        self.frame_find_and_replace.setMinimumSize(QSize(0, 0))
        self.frame_find_and_replace.setMaximumSize(QSize(16777215, 60))
        self.frame_find_and_replace.setStyleSheet(u"QFrame#frame_find_and_replace {\n"
"	background-color: white;\n"
"	border-bottom: 1px solid rgb(224, 224, 224);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: white;\n"
"	border: 1px solid rgb(164, 164, 164);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(224, 224, 224);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	margin: 0;\n"
"	color: black;\n"
"	border-radius: 4px;\n"
"	border: 1px solid rgb(224, 224, 224);\n"
"}\n"
"\n"
"QLineEdit#line_find {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"	border-right: 0;\n"
"\n"
"}")
        self.frame_find_and_replace.setFrameShape(QFrame.StyledPanel)
        self.frame_find_and_replace.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_find_and_replace)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 8, 8, 5)
        self.frame_find = QFrame(self.frame_find_and_replace)
        self.frame_find.setObjectName(u"frame_find")
        self.frame_find.setMinimumSize(QSize(0, 20))
        self.frame_find.setMaximumSize(QSize(16777215, 25))
        self.frame_find.setStyleSheet(u"")
        self.frame_find.setFrameShape(QFrame.StyledPanel)
        self.frame_find.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_find)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_find)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 16))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.line_find = QLineEdit(self.frame)
        self.line_find.setObjectName(u"line_find")
        self.line_find.setMinimumSize(QSize(0, 16))
        self.line_find.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setPointSize(11)
        self.line_find.setFont(font6)
        self.line_find.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.line_find)

        self.label_find_count = QLabel(self.frame)
        self.label_find_count.setObjectName(u"label_find_count")
        self.label_find_count.setMinimumSize(QSize(63, 16))
        self.label_find_count.setMaximumSize(QSize(63, 16))
        self.label_find_count.setFont(font6)
        self.label_find_count.setStyleSheet(u"border: 1px solid rgb(224, 224, 224);\n"
"border-left: 0;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"color: rgb(184, 184, 184);")
        self.label_find_count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_find_count)


        self.horizontalLayout_8.addWidget(self.frame)

        self.frame_find_control_buttons = QFrame(self.frame_find)
        self.frame_find_control_buttons.setObjectName(u"frame_find_control_buttons")
        self.frame_find_control_buttons.setMinimumSize(QSize(0, 17))
        self.frame_find_control_buttons.setMaximumSize(QSize(40, 17))
        self.frame_find_control_buttons.setStyleSheet(u"QPushButton#button_next {\n"
"	border-left: 0;\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_prev {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}")
        self.frame_find_control_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_find_control_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_find_control_buttons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_prev = QPushButton(self.frame_find_control_buttons)
        self.button_prev.setObjectName(u"button_prev")
        self.button_prev.setMinimumSize(QSize(0, 16))
        self.button_prev.setMaximumSize(QSize(20, 16))
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_prev.setIcon(icon)
        self.button_prev.setIconSize(QSize(13, 13))

        self.horizontalLayout_4.addWidget(self.button_prev)

        self.button_next = QPushButton(self.frame_find_control_buttons)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMinimumSize(QSize(0, 16))
        self.button_next.setMaximumSize(QSize(20, 16))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_next.setIcon(icon1)
        self.button_next.setIconSize(QSize(13, 13))

        self.horizontalLayout_4.addWidget(self.button_next)


        self.horizontalLayout_8.addWidget(self.frame_find_control_buttons)

        self.button_done = QPushButton(self.frame_find)
        self.button_done.setObjectName(u"button_done")
        self.button_done.setMinimumSize(QSize(45, 16))
        self.button_done.setMaximumSize(QSize(54, 16))
        self.button_done.setFont(font6)

        self.horizontalLayout_8.addWidget(self.button_done)

        self.check_regex = QCheckBox(self.frame_find)
        self.check_regex.setObjectName(u"check_regex")
        self.check_regex.setMinimumSize(QSize(63, 16))
        self.check_regex.setMaximumSize(QSize(63, 16))
        self.check_regex.setFont(font6)

        self.horizontalLayout_8.addWidget(self.check_regex)

        self.check_replace = QCheckBox(self.frame_find)
        self.check_replace.setObjectName(u"check_replace")
        self.check_replace.setMinimumSize(QSize(0, 16))
        self.check_replace.setMaximumSize(QSize(16777215, 16))
        self.check_replace.setFont(font6)
        self.check_replace.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.check_replace)


        self.verticalLayout_2.addWidget(self.frame_find)

        self.frame_replace = QFrame(self.frame_find_and_replace)
        self.frame_replace.setObjectName(u"frame_replace")
        self.frame_replace.setMinimumSize(QSize(0, 16))
        self.frame_replace.setMaximumSize(QSize(16777215, 20))
        self.frame_replace.setFrameShape(QFrame.StyledPanel)
        self.frame_replace.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_replace)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.line_replace = QLineEdit(self.frame_replace)
        self.line_replace.setObjectName(u"line_replace")
        self.line_replace.setMinimumSize(QSize(0, 16))
        self.line_replace.setMaximumSize(QSize(16777215, 16))
        self.line_replace.setFont(font6)

        self.horizontalLayout_6.addWidget(self.line_replace)

        self.frame_replace_all_buttons = QFrame(self.frame_replace)
        self.frame_replace_all_buttons.setObjectName(u"frame_replace_all_buttons")
        self.frame_replace_all_buttons.setMinimumSize(QSize(0, 17))
        self.frame_replace_all_buttons.setMaximumSize(QSize(16777215, 17))
        self.frame_replace_all_buttons.setStyleSheet(u"QPushButton#button_all {\n"
"	border-left: 0;\n"
"	border-top-left-radius: 0;\n"
"	border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"QPushButton#button_replace {\n"
"	border-top-right-radius: 0;\n"
"	border-bottom-right-radius: 0;\n"
"}")
        self.frame_replace_all_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_replace_all_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_replace_all_buttons)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_replace = QPushButton(self.frame_replace_all_buttons)
        self.button_replace.setObjectName(u"button_replace")
        self.button_replace.setMinimumSize(QSize(60, 16))
        self.button_replace.setMaximumSize(QSize(60, 16))
        self.button_replace.setFont(font6)
        self.button_replace.setIconSize(QSize(13, 13))

        self.horizontalLayout_7.addWidget(self.button_replace)

        self.button_all = QPushButton(self.frame_replace_all_buttons)
        self.button_all.setObjectName(u"button_all")
        self.button_all.setMinimumSize(QSize(30, 16))
        self.button_all.setMaximumSize(QSize(30, 16))
        self.button_all.setFont(font6)
        self.button_all.setIconSize(QSize(13, 13))

        self.horizontalLayout_7.addWidget(self.button_all)


        self.horizontalLayout_6.addWidget(self.frame_replace_all_buttons)

        self.button_done_2 = QPushButton(self.frame_replace)
        self.button_done_2.setObjectName(u"button_done_2")
        self.button_done_2.setMinimumSize(QSize(45, 16))
        self.button_done_2.setMaximumSize(QSize(54, 16))
        self.button_done_2.setFont(font6)

        self.horizontalLayout_6.addWidget(self.button_done_2)


        self.verticalLayout_2.addWidget(self.frame_replace)


        self.verticalLayout.addWidget(self.frame_find_and_replace)

        self.scrollArea = QScrollArea(self.central_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 770, 264))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.central_widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 770, 24))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menuRecent = QMenu(self.menu_file)
        self.menuRecent.setObjectName(u"menuRecent")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_find = QMenu(self.menu_edit)
        self.menu_find.setObjectName(u"menu_find")
        self.menu_format = QMenu(self.menubar)
        self.menu_format.setObjectName(u"menu_format")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_window = QMenu(self.menubar)
        self.menu_window.setObjectName(u"menu_window")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_format.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_window.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.menuRecent.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_rename)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_print)
        self.menu_edit.addAction(self.action_cut)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.action_paste)
        self.menu_edit.addAction(self.action_delete)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menu_find.menuAction())
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_paste_link)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.action_redo)
        self.menu_edit.addAction(self.action_undo)
        self.menu_find.addAction(self.action_find)
        self.menu_find.addAction(self.action_find_and_replace)
        self.menu_format.addAction(self.action_bold)
        self.menu_format.addAction(self.action_italic)
        self.menu_format.addAction(self.action_underline)
        self.menu_format.addSeparator()
        self.menu_format.addAction(self.action_left)
        self.menu_format.addAction(self.action_center)
        self.menu_format.addAction(self.action_right)
        self.menu_format.addAction(self.action_justify)
        self.menu_format.addSeparator()
        self.menu_format.addAction(self.action_indent)
        self.menu_format.addAction(self.action_unindent)

        self.retranslateUi(MainWindow)
        self.check_replace.toggled.connect(self.frame_replace.setVisible)
        self.check_replace.toggled.connect(self.button_done.setHidden)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R&R Text Editor", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.action_rename.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.action_cut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.action_paste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.action_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.action_find.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.action_find_and_replace.setText(QCoreApplication.translate("MainWindow", u"Find and Replace", None))
        self.action_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.action_paste_link.setText(QCoreApplication.translate("MainWindow", u"Paste link...", None))
        self.action_bold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.action_italic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.action_underline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.action_left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.action_center.setText(QCoreApplication.translate("MainWindow", u"Center", None))
        self.action_right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.action_justify.setText(QCoreApplication.translate("MainWindow", u"Justify", None))
        self.action_indent.setText(QCoreApplication.translate("MainWindow", u"Indent", None))
        self.action_unindent.setText(QCoreApplication.translate("MainWindow", u"Unindent", None))
        self.action_redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(tooltip)
        self.combo_box_fonts.setToolTip(QCoreApplication.translate("MainWindow", u"Font", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.combo_box_styles.setToolTip(QCoreApplication.translate("MainWindow", u"Styles", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spin_box_size.setToolTip(QCoreApplication.translate("MainWindow", u"Text Size", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.widget_color_picker.setToolTip(QCoreApplication.translate("MainWindow", u"Text Color", None))
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
        self.line_find.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.label_find_count.setText(QCoreApplication.translate("MainWindow", u"1000/1000", None))
        self.button_prev.setText("")
        self.button_next.setText("")
        self.button_done.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.check_regex.setText(QCoreApplication.translate("MainWindow", u"Regex", None))
        self.check_replace.setText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.line_replace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Replace", None))
        self.button_replace.setText(QCoreApplication.translate("MainWindow", u"Repalce", None))
        self.button_all.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.button_done_2.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuRecent.setTitle(QCoreApplication.translate("MainWindow", u"Recent", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menu_find.setTitle(QCoreApplication.translate("MainWindow", u"Find", None))
        self.menu_format.setTitle(QCoreApplication.translate("MainWindow", u"Format", None))
        self.menu_settings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menu_window.setTitle(QCoreApplication.translate("MainWindow", u"Window", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

