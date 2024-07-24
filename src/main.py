import os
import sys

from PySide6.QtCore import QSize, QEvent
from PySide6.QtGui import QIcon, Qt, QColor, QFont
from PySide6.QtWidgets import QMainWindow, QApplication, QColorDialog, QTextEdit, QMessageBox

from design import Ui_MainWindow
from service_files import FileManager

import rc.resources

# RECENT_FILES = []


class TextEditor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.file_manager = FileManager(self.ui.text_edit)

        self._set_icons_svg()
        self._init_setup()

    def _set_icons_svg(self):
        # Calcite Sharp Line Icons Collection
        # https://www.svgrepo.com/collection/calcite-sharp-line-icons/14

        icon_left = QIcon()
        icon_left.addFile(":icons/icons/left.svg", QSize(), QIcon.Normal)
        self.ui.button_left.setIcon(icon_left)
        self.ui.button_left.setIconSize(QSize(12, 12))

        icon_center = QIcon()
        icon_center.addFile(":icons/icons/center.svg", QSize(), QIcon.Normal)
        self.ui.button_center.setIcon(icon_center)
        self.ui.button_center.setIconSize(QSize(12, 12))

        icon_right = QIcon()
        icon_right.addFile(":icons/icons/right.svg", QSize(), QIcon.Normal)
        self.ui.button_right.setIcon(icon_right)
        self.ui.button_right.setIconSize(QSize(12, 12))

        icon_justify = QIcon()
        icon_justify.addFile(":icons/icons/justify.svg", QSize(), QIcon.Normal)
        self.ui.button_justify.setIcon(icon_justify)
        self.ui.button_justify.setIconSize(QSize(12, 12))

        icon_spacing = QIcon()
        icon_spacing.addFile(":icons/icons/spacing.svg", QSize(), QIcon.Normal)
        self.ui.button_spacing.setIcon(icon_spacing)
        self.ui.button_spacing.setIconSize(QSize(12, 12))

    def _init_setup(self):

        self.ui.widget_color_picker.installEventFilter(self)
        self.ui.widget_color_picker.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.ui.widget_color.setAutoFillBackground(True)

        self.ui.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.ui.text_edit.selectionChanged.connect(self.update_format)

        self.ui.combo_box_fonts.currentFontChanged.connect(self.ui.text_edit.setCurrentFont)
        self.ui.spin_box_size.valueChanged.connect(lambda s: self.ui.text_edit.setFontPointSize(float(s)))

        self.ui.button_left.toggled.connect(lambda: self.ui.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.ui.button_center.toggled.connect(lambda: self.ui.text_edit.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.ui.button_right.toggled.connect(lambda: self.ui.text_edit.setAlignment(Qt.AlignmentFlag.AlignRight))
        self.ui.button_justify.toggled.connect(lambda: self.ui.text_edit.setAlignment(Qt.AlignmentFlag.AlignJustify))

        self.ui.button_bold.toggled.connect(
            lambda x: self.ui.text_edit.setFontWeight(QFont.Weight.Bold if x else QFont.Weight.Normal))
        self.ui.button_italic.toggled.connect(lambda x: self.ui.text_edit.setFontItalic(True if x else False))
        self.ui.button_underline.toggled.connect(lambda x: self.ui.text_edit.setFontUnderline(True if x else False))

        self.ui.action_close.triggered.connect(self.close)
        self.ui.action_new.triggered.connect(self.new_file_event)
        self.ui.action_open.triggered.connect(self.open_file_event)
        self.ui.action_save.triggered.connect(self.save_file_event)

        self.ui.action_cut.triggered.connect(self.ui.text_edit.cut)
        self.ui.action_copy.triggered.connect(self.ui.text_edit.copy)
        self.ui.action_paste.triggered.connect(self.ui.text_edit.paste)
        self.ui.action_delete.triggered.connect(self.delete_event)

        self.ui.spin_box_size.setValue(12)
        self.ui.text_edit.setFontItalic(False)
        self.ui.text_edit.setFontUnderline(False)
        self.ui.text_edit.setTextColor(QColor("black"))
        self.ui.text_edit.setFontWeight(QFont.Weight.Normal)
        self.ui.combo_box_fonts.setCurrentFont("Times New Roman")
        self.ui.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.set_current_color(QColor('black'))

        font = QFont("Times New Roman", 12)
        self.ui.text_edit.setFont(font)
        self.ui.text_edit.setFontPointSize(12)

        self.ui.widget_color_picker.setStyleSheet(
            "QWidget#widget_color_picker{background-color: rgb(244, 244, 244);}")

        self.update_format()
        self._update_title()

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
    
    def delete_event(self):
        cursor = self.ui.text_edit.textCursor()
        cursor.removeSelectedText()

    def new_file_event(self):
        self._default_settings()
        self._update_title()
    
    def open_file_event(self):
        self.file_manager.open_file()
        self._update_title()
    
    def save_file_event(self):
        self.file_manager.save_file()
        self._update_title()
    
    def _update_title(self):
        self.setWindowTitle("%s - R&R Text Editor" % (os.path.basename(self.file_manager.file_path)
                                                      if self.file_manager.file_path else "Untitled"))

    def _default_settings(self):
        self.file_manager.file_path = None
        self.ui.text_edit.clear()

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

        self.ui.combo_box_fonts.setCurrentFont(self.ui.text_edit.currentFont())
        self.ui.spin_box_size.setValue(int(self.ui.text_edit.fontPointSize()))

        self.ui.button_bold.setChecked(self.ui.text_edit.fontWeight() == QFont.Weight.Bold)
        self.ui.button_italic.setChecked(self.ui.text_edit.fontItalic())
        self.ui.button_underline.setChecked(self.ui.text_edit.fontUnderline())

        self.ui.button_left.setChecked(self.ui.text_edit.alignment() == Qt.AlignmentFlag.AlignLeft)
        self.ui.button_center.setChecked(self.ui.text_edit.alignment() == Qt.AlignmentFlag.AlignCenter)
        self.ui.button_right.setChecked(self.ui.text_edit.alignment() == Qt.AlignmentFlag.AlignRight)
        self.ui.button_justify.setChecked(self.ui.text_edit.alignment() == Qt.AlignmentFlag.AlignJustify)

        self.set_current_color(self.ui.text_edit.textColor())

        self.block_signals(signals, False)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.set_current_color(color)
        self.ui.text_edit.setTextColor(color)

    def set_current_color(self, color: QColor):
        self.ui.widget_color.setStyleSheet(f"background-color: {color.name(QColor.NameFormat.HexRgb)};")

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Application Close',
                                     'Do you want to save the current document?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.Yes)
        
        if reply == QMessageBox.StandardButton.No:
            event.accept()
        else:
            # self.save_file()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
