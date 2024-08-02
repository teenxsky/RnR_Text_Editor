# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spacing.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDialog,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_DialogSpacing(object):
    def setupUi(self, DialogSpacing):
        if not DialogSpacing.objectName():
            DialogSpacing.setObjectName(u"DialogSpacing")
        DialogSpacing.resize(370, 245)
        DialogSpacing.setMinimumSize(QSize(370, 245))
        DialogSpacing.setMaximumSize(QSize(370, 245))
        DialogSpacing.setStyleSheet(u"QDialog {\n"
"	background-color: white;\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QDoubleSpinBox {\n"
"	width: 30px;\n"
"\n"
"}\n"
"\n"
"QFrame {\n"
"	border: 0;\n"
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
"}")
        self.verticalLayout_2 = QVBoxLayout(DialogSpacing)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 10, 15, 10)
        self.frame_mul = QFrame(DialogSpacing)
        self.frame_mul.setObjectName(u"frame_mul")
        self.frame_mul.setMinimumSize(QSize(0, 25))
        self.frame_mul.setMaximumSize(QSize(16777215, 30))
        self.frame_mul.setFrameShape(QFrame.StyledPanel)
        self.frame_mul.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_mul)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_mul)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 20))
        self.label_2.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.spin_prop_height = QSpinBox(self.frame_mul)
        self.spin_prop_height.setObjectName(u"spin_prop_height")
        self.spin_prop_height.setMinimumSize(QSize(60, 20))
        self.spin_prop_height.setMaximumSize(QSize(60, 25))
        font1 = QFont()
        font1.setPointSize(11)
        self.spin_prop_height.setFont(font1)
        self.spin_prop_height.setMaximum(1000)

        self.horizontalLayout.addWidget(self.spin_prop_height)

        self.label = QLabel(self.frame_mul)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(35, 20))
        self.label.setMaximumSize(QSize(35, 20))
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_mul)

        self.frame_3 = QFrame(DialogSpacing)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 65))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 0, 0, 2, 1)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_line_height_radio_buttons = QFrame(self.frame)
        self.frame_line_height_radio_buttons.setObjectName(u"frame_line_height_radio_buttons")
        self.frame_line_height_radio_buttons.setMinimumSize(QSize(80, 30))
        self.frame_line_height_radio_buttons.setMaximumSize(QSize(80, 55))
        self.frame_line_height_radio_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_line_height_radio_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_line_height_radio_buttons)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_fixed = QRadioButton(self.frame_line_height_radio_buttons)
        self.group_line_height = QButtonGroup(DialogSpacing)
        self.group_line_height.setObjectName(u"group_line_height")
        self.group_line_height.addButton(self.radio_fixed)
        self.radio_fixed.setObjectName(u"radio_fixed")
        self.radio_fixed.setMinimumSize(QSize(80, 20))
        self.radio_fixed.setMaximumSize(QSize(80, 20))
        self.radio_fixed.setFont(font1)

        self.verticalLayout.addWidget(self.radio_fixed)

        self.radio_min = QRadioButton(self.frame_line_height_radio_buttons)
        self.group_line_height.addButton(self.radio_min)
        self.radio_min.setObjectName(u"radio_min")
        self.radio_min.setMinimumSize(QSize(80, 20))
        self.radio_min.setMaximumSize(QSize(80, 20))
        self.radio_min.setFont(font1)

        self.verticalLayout.addWidget(self.radio_min)


        self.horizontalLayout_2.addWidget(self.frame_line_height_radio_buttons)

        self.horizontalSpacer_2 = QSpacerItem(83, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.spin_line_height_1 = QDoubleSpinBox(self.frame)
        self.spin_line_height_1.setObjectName(u"spin_line_height_1")
        self.spin_line_height_1.setMinimumSize(QSize(60, 20))
        self.spin_line_height_1.setMaximumSize(QSize(60, 25))
        self.spin_line_height_1.setFont(font1)
        self.spin_line_height_1.setMinimum(-99.000000000000000)
        self.spin_line_height_1.setMaximum(10000.000000000000000)

        self.horizontalLayout_2.addWidget(self.spin_line_height_1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(35, 20))
        self.label_3.setMaximumSize(QSize(35, 20))
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 25))
        self.frame_2.setMaximumSize(QSize(16777215, 25))
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.check_max = QCheckBox(self.frame_2)
        self.check_max.setObjectName(u"check_max")
        self.check_max.setMinimumSize(QSize(0, 20))
        self.check_max.setMaximumSize(QSize(16777215, 20))
        self.check_max.setFont(font1)

        self.horizontalLayout_3.addWidget(self.check_max)

        self.horizontalSpacer_3 = QSpacerItem(96, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.spin_line_height_2 = QDoubleSpinBox(self.frame_2)
        self.spin_line_height_2.setObjectName(u"spin_line_height_2")
        self.spin_line_height_2.setMinimumSize(QSize(60, 20))
        self.spin_line_height_2.setMaximumSize(QSize(60, 25))
        self.spin_line_height_2.setFont(font1)
        self.spin_line_height_2.setMinimum(-99.000000000000000)
        self.spin_line_height_2.setMaximum(10000.000000000000000)

        self.horizontalLayout_3.addWidget(self.spin_line_height_2)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(35, 20))
        self.label_4.setMaximumSize(QSize(35, 20))
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)


        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(DialogSpacing)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 25))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.horizontalSpacer_4 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.spin_line_distance = QDoubleSpinBox(self.frame_4)
        self.spin_line_distance.setObjectName(u"spin_line_distance")
        self.spin_line_distance.setMinimumSize(QSize(60, 20))
        self.spin_line_distance.setMaximumSize(QSize(60, 25))
        self.spin_line_distance.setFont(font1)
        self.spin_line_distance.setMinimum(-99.000000000000000)
        self.spin_line_distance.setMaximum(10000.000000000000000)

        self.horizontalLayout_4.addWidget(self.spin_line_distance)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(35, 20))
        self.label_6.setMaximumSize(QSize(35, 20))
        self.label_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_6)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_7 = QFrame(DialogSpacing)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.frame_7.setFont(font2)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 20))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font1)
        self.label_12.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 2, 1)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 20))
        self.frame_9.setMaximumSize(QSize(16777215, 25))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 20))
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_13)

        self.spin_par_spacing_left = QDoubleSpinBox(self.frame_9)
        self.spin_par_spacing_left.setObjectName(u"spin_par_spacing_left")
        self.spin_par_spacing_left.setMinimumSize(QSize(60, 20))
        self.spin_par_spacing_left.setMaximumSize(QSize(60, 25))
        self.spin_par_spacing_left.setFont(font1)
        self.spin_par_spacing_left.setMaximum(10000.000000000000000)

        self.horizontalLayout_8.addWidget(self.spin_par_spacing_left)

        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(35, 20))
        self.label_14.setMaximumSize(QSize(35, 20))
        self.label_14.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_14)


        self.gridLayout_2.addWidget(self.frame_9, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 20))
        self.frame_5.setMaximumSize(QSize(16777215, 25))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.spin_par_spacing_top = QDoubleSpinBox(self.frame_5)
        self.spin_par_spacing_top.setObjectName(u"spin_par_spacing_top")
        self.spin_par_spacing_top.setMinimumSize(QSize(60, 20))
        self.spin_par_spacing_top.setMaximumSize(QSize(60, 25))
        self.spin_par_spacing_top.setFont(font1)
        self.spin_par_spacing_top.setMaximum(10000.000000000000000)

        self.horizontalLayout_5.addWidget(self.spin_par_spacing_top)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(35, 20))
        self.label_8.setMaximumSize(QSize(35, 20))
        self.label_8.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.gridLayout_2.addWidget(self.frame_5, 0, 2, 1, 1)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 25))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.spin_par_spacing_right = QDoubleSpinBox(self.frame_10)
        self.spin_par_spacing_right.setObjectName(u"spin_par_spacing_right")
        self.spin_par_spacing_right.setMinimumSize(QSize(60, 20))
        self.spin_par_spacing_right.setMaximumSize(QSize(60, 25))
        self.spin_par_spacing_right.setFont(font1)
        self.spin_par_spacing_right.setMaximum(10000.000000000000000)

        self.horizontalLayout_9.addWidget(self.spin_par_spacing_right)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(35, 20))
        self.label_16.setMaximumSize(QSize(35, 20))
        self.label_16.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_16)


        self.gridLayout_2.addWidget(self.frame_10, 1, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 25))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.spin_par_spacing_bottom = QDoubleSpinBox(self.frame_6)
        self.spin_par_spacing_bottom.setObjectName(u"spin_par_spacing_bottom")
        self.spin_par_spacing_bottom.setMinimumSize(QSize(60, 20))
        self.spin_par_spacing_bottom.setMaximumSize(QSize(60, 25))
        self.spin_par_spacing_bottom.setFont(font1)
        self.spin_par_spacing_bottom.setMaximum(10000.000000000000000)

        self.horizontalLayout_6.addWidget(self.spin_par_spacing_bottom)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(35, 20))
        self.label_11.setMaximumSize(QSize(35, 20))
        self.label_11.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_11)


        self.gridLayout_2.addWidget(self.frame_6, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(DialogSpacing)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 20))
        self.frame_8.setMaximumSize(QSize(16777215, 25))
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
        self.button_cancel.setFont(font1)

        self.horizontalLayout_7.addWidget(self.button_cancel)

        self.button_ok = QPushButton(self.frame_8)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setMinimumSize(QSize(70, 18))
        self.button_ok.setMaximumSize(QSize(70, 18))
        self.button_ok.setFont(font1)

        self.horizontalLayout_7.addWidget(self.button_ok)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.retranslateUi(DialogSpacing)
        self.radio_fixed.toggled.connect(self.check_max.setDisabled)
        self.check_max.toggled.connect(self.spin_line_height_2.setEnabled)

        QMetaObject.connectSlotsByName(DialogSpacing)
    # setupUi

    def retranslateUi(self, DialogSpacing):
        DialogSpacing.setWindowTitle(QCoreApplication.translate("DialogSpacing", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("DialogSpacing", u"This sets the spacing proportional to the line (in percentage). For example, set to 200 for double spacing.", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("DialogSpacing", u"Proportional Height", None))
        self.label.setText(QCoreApplication.translate("DialogSpacing", u"%", None))
        self.label_5.setText(QCoreApplication.translate("DialogSpacing", u"Line height", None))
#if QT_CONFIG(tooltip)
        self.radio_fixed.setToolTip(QCoreApplication.translate("DialogSpacing", u"This sets the line height to a fixed line height (in pixels)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_fixed.setText(QCoreApplication.translate("DialogSpacing", u"Fixed", None))
#if QT_CONFIG(tooltip)
        self.radio_min.setToolTip(QCoreApplication.translate("DialogSpacing", u"This sets the minimum line height (in pixels)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_min.setText(QCoreApplication.translate("DialogSpacing", u"Minimum", None))
        self.label_3.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
        self.check_max.setText(QCoreApplication.translate("DialogSpacing", u"Maximum", None))
        self.label_4.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("DialogSpacing", u"This adds the specified height between lines (in pixels)", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("DialogSpacing", u"Line Distance Height", None))
        self.label_6.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("DialogSpacing", u"Sets the paragraph's alignment", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("DialogSpacing", u"Paragraph spacing", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("DialogSpacing", u"Sets the paragraph's left margin", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("DialogSpacing", u"left", None))
        self.label_14.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("DialogSpacing", u"Sets the paragraph's top margin", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("DialogSpacing", u"top", None))
        self.label_8.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
#if QT_CONFIG(tooltip)
        self.label_15.setToolTip(QCoreApplication.translate("DialogSpacing", u"Sets the paragraph's right margin", None))
#endif // QT_CONFIG(tooltip)
        self.label_15.setText(QCoreApplication.translate("DialogSpacing", u"right", None))
        self.label_16.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("DialogSpacing", u"Sets the paragraph's bottom margin", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("DialogSpacing", u"bottom", None))
        self.label_11.setText(QCoreApplication.translate("DialogSpacing", u"pixels", None))
        self.button_cancel.setText(QCoreApplication.translate("DialogSpacing", u"Cancel", None))
        self.button_ok.setText(QCoreApplication.translate("DialogSpacing", u"OK", None))
    # retranslateUi

