import sys

from PySide6.QtCore import QSize, QEvent
from PySide6.QtGui import QIcon, Qt, QPalette, QColor, QFont
from PySide6.QtWidgets import QMainWindow, QApplication, QColorDialog, QTextEdit

from design import Ui_MainWindow

import rc.resources


class TextEditor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._set_icons_svg()
        self._init_setup()

    def _set_icons_svg(self):

        # Calcite Sharp Line Icons Collection
        # https://www.svgrepo.com/collection/calcite-sharp-line-icons/14

        icon_left = QIcon()
        icon_left.addFile(":icons/icons/left.svg", QSize(), QIcon.Normal)
        self.ui.button_left.setIcon(icon_left)
        self.ui.button_left.setIconSize(QSize(16, 16))

        icon_center = QIcon()
        icon_center.addFile(":icons/icons/center.svg", QSize(), QIcon.Normal)
        self.ui.button_center.setIcon(icon_center)
        self.ui.button_center.setIconSize(QSize(16, 16))

        icon_right = QIcon()
        icon_right.addFile(":icons/icons/right.svg", QSize(), QIcon.Normal)
        self.ui.button_right.setIcon(icon_right)
        self.ui.button_right.setIconSize(QSize(16, 16))

        icon_justify = QIcon()
        icon_justify.addFile(":icons/icons/justify.svg", QSize(), QIcon.Normal)
        self.ui.button_justify.setIcon(icon_justify)
        self.ui.button_justify.setIconSize(QSize(16, 16))

        icon_spacing = QIcon()
        icon_spacing.addFile(":icons/icons/spacing.svg", QSize(), QIcon.Normal)
        self.ui.button_spacing.setIcon(icon_spacing)
        self.ui.button_spacing.setIconSize(QSize(16, 16))

    def _init_setup(self):

        self.ui.textEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.ui.textEdit.selectionChanged.connect(self.update_format)
        font = QFont("Times New Roman", 12)
        self.ui.textEdit.setFont(font)
        self.ui.textEdit.setFontPointSize(12)

        self.ui.widget_color_picker.setStyleSheet(
            "QWidget#widget_color_picker{background-color: rgb(244, 244, 244);}")

        self.ui.widget_color_picker.installEventFilter(self)
        self.ui.widget_color_picker.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.ui.widget_color.setAutoFillBackground(True)

        self.ui.combo_box_fonts.currentFontChanged.connect(self.ui.textEdit.setCurrentFont)
        self.ui.spin_box_size.valueChanged.connect(lambda s: self.ui.textEdit.setFontPointSize(float(s)))

        self.ui.button_left.toggled.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.ui.button_center.toggled.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.ui.button_right.toggled.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignmentFlag.AlignRight))
        self.ui.button_justify.toggled.connect(lambda: self.ui.textEdit.setAlignment(Qt.AlignmentFlag.AlignJustify))

        self.ui.button_bold.toggled.connect(
            lambda x: self.ui.textEdit.setFontWeight(QFont.Weight.Bold if x else QFont.Weight.Normal))
        self.ui.button_italic.toggled.connect(lambda: self.ui.textEdit.setFontItalic)
        self.ui.button_underline.toggled.connect(lambda: self.ui.textEdit.setFontUnderline)

        self.update_format()

    def eventFilter(self, watched, event):

        if watched == self.ui.widget_color_picker:

            if event.type() == QEvent.Type.HoverLeave:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(244, 244, 244);}")

            elif event.type() == QEvent.Type.HoverEnter:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(234, 234, 234);}")

            elif event.type() == QEvent.Type.MouseButtonPress:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(224, 224, 224);}")
                self.color_picker()

            return True

    @staticmethod
    def block_signals(objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):

        signals = [
            self.ui.combo_box_fonts,
            self.ui.spin_box_size,
            self.ui.button_bold,
            self.ui.button_italic,
            self.ui.button_underline,
        ]

        self.block_signals(signals, True)

        self.ui.combo_box_fonts.setCurrentFont(self.ui.textEdit.currentFont())
        self.ui.spin_box_size.setValue(int(self.ui.textEdit.fontPointSize()))

        self.ui.button_bold.setChecked(self.ui.textEdit.fontWeight() == QFont.Weight.Bold)
        self.ui.button_italic.setChecked(self.ui.textEdit.fontItalic())
        self.ui.button_underline.setChecked(self.ui.textEdit.fontUnderline())

        self.ui.button_left.setChecked(self.ui.textEdit.alignment() == Qt.AlignmentFlag.AlignLeft)
        self.ui.button_center.setChecked(self.ui.textEdit.alignment() == Qt.AlignmentFlag.AlignCenter)
        self.ui.button_right.setChecked(self.ui.textEdit.alignment() == Qt.AlignmentFlag.AlignRight)
        self.ui.button_justify.setChecked(self.ui.textEdit.alignment() == Qt.AlignmentFlag.AlignJustify)

        self.set_current_color(self.ui.textEdit.textColor())

        self.block_signals(signals, False)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.set_current_color(color)
        self.ui.textEdit.setTextColor(color)

    def set_current_color(self, c: QColor):
        self.ui.widget_color.setStyleSheet(f"background-color: {c.name(QColor.NameFormat.HexRgb)};")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
