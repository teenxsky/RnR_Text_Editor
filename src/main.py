import os
import sys
import uuid

from PySide6.QtCore import QSize, QEvent, QCoreApplication, QPoint, Signal, QRegularExpression, QDir
from PySide6.QtGui import QIcon, Qt, QColor, QFont, QKeySequence, QAction, QFontDatabase, QImage, QTextDocument, \
    QTextCharFormat, QBrush, QTextCursor
from PySide6.QtWidgets import QMainWindow, QApplication, QColorDialog, QTextEdit, QMessageBox, QDialog, QWidget

from design import Ui_MainWindow, Ui_DialogSpacing, Ui_Dialog
from service_files import FileManager, get_info, add_recent_file, remove_recent_file

import rc.resources

RECENT_FILE_ACTIONS = []
IMAGE_EXTENSIONS = ['.jpg', '.png', '.bmp']


class TextEdit(QTextEdit):

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return super(TextEdit, self).canInsertFromMimeData(source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = os.path.splitext(str(u.toLocalFile()))[1].lower()
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(QTextDocument.ResourceType.ImageResource, u, image)
                    cursor.insertImage(u.toLocalFile())

                else:
                    break

            else:
                return

        elif source.hasImage():
            image = source.imageData()
            UUID = uuid.uuid4().hex
            document.addResource(QTextDocument.ResourceType.ImageResource, UUID, image)
            cursor.insertImage(UUID)
            return

        super(TextEdit, self).insertFromMimeData(source)


class RenameWidget(Ui_Dialog, QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Rename File")
        self.setFixedSize(470, 80)

    def get_filename(self):
        return self.ui.lineEdit.text()

    def set_filename(self, filename: str):
        self.ui.lineEdit.setText(filename)


class SpacingDialog(Ui_DialogSpacing, QDialog):

    cancel_clicked = Signal()
    ok_clicked = Signal()

    def __init__(self, parent: QWidget):
        super(Ui_DialogSpacing, self).__init__()

        self.ui = Ui_DialogSpacing()
        self.ui.setupUi(self)

        self.setParent(parent)
        self.move(QPoint(parent.size().width() // 2 - self.size().width() // 2,
                         parent.size().height() // 2 - self.size().height() // 2))

        self.ui.radio_min.setChecked(True)
        self.ui.check_max.setChecked(False)

        self.ui.button_cancel.clicked.connect(self.cancel_clicked.emit)
        self.ui.button_ok.clicked.connect(self.ok_clicked.emit)


class FindAndReplaceWidget:
    def __init__(self, ui: Ui_MainWindow, text_edit: QTextEdit):
        self.ui = ui
        self.ui.frame_find_and_replace.setHidden(True)

        self.ui.line_find.textChanged.connect(self.find_event)
        self.ui.button_done.clicked.connect(self.close_widget)
        self.ui.button_done_2.clicked.connect(self.close_widget)
        self.ui.check_regex.clicked.connect(self._set_regex_mode)
        self.ui.button_replace.clicked.connect(self.replace_event)
        self.ui.button_all.clicked.connect(self.replace_all_event)
        self.ui.button_next.clicked.connect(self._show_finded_next_occurrence)
        self.ui.button_prev.clicked.connect(self._show_finded_previous_occurrence)

        self.show_format = QTextCharFormat()
        self.block_format = QTextCharFormat()
        self.show_format.setBackground(QBrush(QColor("yellow")))

        self.text_edit = text_edit

        self.cursor = self.text_edit.textCursor()

        self.regex = QRegularExpression()
        self.indexes_of_occurrences = []
        self.current_occurrence = 0
        self.regex_mode = False

        self._reset_setup()

    def run_find_frame(self):
        self.ui.frame_find_and_replace.setHidden(False)
        self.ui.frame_replace.setHidden(True)

    def run_find_and_replace_frame(self):
        self.ui.frame_find_and_replace.setHidden(False)
        self.ui.frame_replace.setHidden(False)
        self.ui.button_done.setHidden(True)
        self.ui.check_replace.setChecked(True)

    def close_widget(self):
        self.ui.line_find.setText("")
        self.ui.line_replace.setText("")

        self.ui.frame_find_and_replace.setHidden(True)
        self._reset_setup()

    def find_event(self, show_current=True):
        self._reset_setup()

        if self.ui.line_find.text() == "":
            return

        pattern = self.ui.line_find.text()

        if not self.regex_mode:
            pattern = pattern.replace(chr(92), chr(92) + chr(92))
            pattern = pattern.replace('.', chr(92) + '.')
            pattern = pattern.replace('*', chr(92) + '*')
            pattern = pattern.replace('?', chr(92) + '?')
            pattern = pattern.replace('+', chr(92) + '+')
            pattern = pattern.replace('^', chr(92) + '^')
            pattern = pattern.replace('$', chr(92) + '$')
            pattern = pattern.replace('(', chr(92) + '(')
            pattern = pattern.replace(')', chr(92) + '(')
            pattern = pattern.replace('[', chr(92) + '[')
            pattern = pattern.replace(']', chr(92) + ']')
            pattern = pattern.replace('{', chr(92) + '{')
            pattern = pattern.replace('}', chr(92) + '}')

        self.regex.setPattern(pattern)

        if not self.regex.isValid():
            return

        begin_index = 0
        end_index = self.regex.match(self.text_edit.toPlainText(), begin_index).capturedStart()

        while end_index != -1:
            begin_index = end_index + self.regex.match(self.text_edit.toPlainText(), begin_index).capturedLength()
            self.indexes_of_occurrences.append((end_index, begin_index))
            end_index = self.regex.match(self.text_edit.toPlainText(), begin_index).capturedStart()
        
        if len(self.indexes_of_occurrences) != 0 and show_current:
            self._show_occurrence(self.indexes_of_occurrences[0][0],
                                  self.indexes_of_occurrences[0][1])

    def replace_event(self):
        if len(self.indexes_of_occurrences) != 0:
            self._block_show_occurrence()
            old_occurrence_index = self.current_occurrence

            self.cursor.insertText(self.ui.line_replace.text())

            self.find_event()
            self.current_occurrence = old_occurrence_index - 1 \
                if len(self.indexes_of_occurrences) - 1 >= old_occurrence_index \
                else len(self.indexes_of_occurrences) - 1
            self._show_finded_next_occurrence()

    def replace_all_event(self):
        self._block_show_occurrence()
        for _ in range(len(self.indexes_of_occurrences)):
            self.replace_event()

    def _show_finded_previous_occurrence(self):
        self._update_current_occurrence()
        
        if self.current_occurrence != 0:
            self.current_occurrence -= 1
            self._show_occurrence(self.indexes_of_occurrences[self.current_occurrence][0],
                                self.indexes_of_occurrences[self.current_occurrence][1])

    def _show_finded_next_occurrence(self):
        self._update_current_occurrence()

        if self.current_occurrence != len(self.indexes_of_occurrences) - 1 \
                and self.indexes_of_occurrences != []:
            self.current_occurrence += 1
            self._show_occurrence(self.indexes_of_occurrences[self.current_occurrence][0],
                                self.indexes_of_occurrences[self.current_occurrence][1])
    
    def _update_current_occurrence(self):
        self._block_show_occurrence()
        old_occurrence_index = self.current_occurrence
        self.find_event(show_current=False)
        self.current_occurrence = old_occurrence_index \
            if len(self.indexes_of_occurrences) - 1 >= old_occurrence_index \
            else len(self.indexes_of_occurrences) - 1
        if self.current_occurrence != -1:
            self._show_occurrence(self.indexes_of_occurrences[self.current_occurrence][0],
                                    self.indexes_of_occurrences[self.current_occurrence][1])

    def _show_count_occurrences(self):
        self.ui.label_find_count.setText(f"""{str(self.current_occurrence + 1)}/{str(len(self.indexes_of_occurrences))}""")

    def _show_occurrence(self, begin: int, end: int):
        self._block_show_occurrence()
        self.cursor.setPosition(begin, QTextCursor.MoveAnchor)
        self.cursor.setPosition(end, QTextCursor.KeepAnchor)

        self.block_format.setBackground(self.cursor.charFormat().background())
        self.block_format.setFontPointSize(self.cursor.charFormat().fontPointSize())
        self.show_format.setFontPointSize(self.cursor.charFormat().fontPointSize() * 1.5)

        self.text_edit.setTextCursor(self.cursor)
        self.text_edit.textCursor().setCharFormat(self.show_format)

        self._show_count_occurrences()

    def _block_show_occurrence(self):
        self.text_edit.setTextCursor(self.cursor)
        self.text_edit.textCursor().setCharFormat(self.block_format)
        self.cursor.clearSelection()
        self.text_edit.setTextCursor(self.cursor)
        
    def _set_regex_mode(self):
        if self.ui.line_find.placeholderText() == "Find":
            self.ui.line_find.setPlaceholderText("Regex")
            self.regex_mode = True
        else:
            self.ui.line_find.setPlaceholderText("Find")
            self.regex_mode = False

    def _reset_setup(self):
        self.current_occurrence = 0
        self._block_show_occurrence()
        self.indexes_of_occurrences.clear()
        self.ui.label_find_count.setText("0")


class TextEditor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.text_edit = QTextEdit()
        self.rename_widget = RenameWidget()
        self.file_manager = FileManager(self.text_edit)
        self.spacing_dialog = SpacingDialog(self)
        self.find_and_replace_widget = FindAndReplaceWidget(self.ui, self.text_edit)

        self.objects_to_block = [
            self.ui.combo_box_fonts,
            self.ui.spin_box_size,
            self.ui.widget_color,
            self.ui.widget_color_picker,
            self.ui.button_bold,
            self.ui.button_italic,
            self.ui.button_underline,
            self.ui.button_left,
            self.ui.button_center,
            self.ui.button_right,
            self.ui.button_justify,
            self.ui.button_spacing,
            self.ui.line_find,
            self.ui.line_replace,
            self.ui.button_prev,
            self.ui.button_next,
            self.ui.button_done,
            self.ui.button_done_2,
            self.ui.check_replace,
            self.ui.button_replace,
            self.ui.button_all,
            self.text_edit
        ]

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

        self.ui.verticalLayout_3.addWidget(self.text_edit)

        self.spacing_dialog.hide()
        self.spacing_dialog.cancel_clicked.connect(self.close_spacing_dialog)
        self.ui.frame_find_and_replace.setHidden(True)
        self.spacing_dialog.ui.spin_line_height_2.setEnabled(self.spacing_dialog.ui.check_max.isChecked())

        self.ui.widget_color_picker.installEventFilter(self)
        self.ui.widget_color_picker.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.ui.widget_color.setAutoFillBackground(True)

        self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.text_edit.selectionChanged.connect(self.update_format)

        self.ui.combo_box_fonts.currentFontChanged.connect(self.text_edit.setCurrentFont)
        self.ui.spin_box_size.valueChanged.connect(lambda s: self.text_edit.setFontPointSize(float(s)))

        self.ui.button_left.toggled.connect(lambda: self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft))
        self.ui.button_center.toggled.connect(lambda: self.text_edit.setAlignment(Qt.AlignmentFlag.AlignCenter))
        self.ui.button_right.toggled.connect(lambda: self.text_edit.setAlignment(Qt.AlignmentFlag.AlignRight))
        self.ui.button_justify.toggled.connect(lambda: self.text_edit.setAlignment(Qt.AlignmentFlag.AlignJustify))

        self.ui.button_bold.toggled.connect(
            lambda x: self.text_edit.setFontWeight(QFont.Weight.Bold if x else QFont.Weight.Normal))
        self.ui.button_italic.toggled.connect(lambda x: self.text_edit.setFontItalic(True if x else False))
        self.ui.button_underline.toggled.connect(lambda x: self.text_edit.setFontUnderline(True if x else False))

        self.ui.action_close.triggered.connect(self.close)
        self.ui.action_close.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_close.setShortcut(QKeySequence("Ctrl+W"))

        self.ui.action_new.triggered.connect(self.new_file_event)
        self.ui.action_new.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_new.setShortcut(QKeySequence("Ctrl+N"))

        self.ui.action_open.triggered.connect(self.open_file_event)
        self.ui.action_open.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_open.setShortcut(QKeySequence("Ctrl+O"))

        self.ui.action_save.triggered.connect(self.save_file_event)
        self.ui.action_save.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_save.setShortcut(QKeySequence("Ctrl+S"))

        self.ui.action_cut.triggered.connect(self.text_edit.cut)
        self.ui.action_cut.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_cut.setShortcut(QKeySequence("Ctrl+X"))

        self.ui.action_copy.triggered.connect(self.text_edit.copy)
        self.ui.action_copy.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_copy.setShortcut(QKeySequence("Ctrl+C"))

        self.ui.action_paste.triggered.connect(self.text_edit.paste)
        self.ui.action_paste.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_paste.setShortcut(QKeySequence("Ctrl+V"))

        # self.ui.action_print.triggered.connect(self.text_edit.paste)
        self.ui.action_print.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_print.setShortcut(QKeySequence("Ctrl+P"))

        self.ui.action_delete.triggered.connect(self.delete_event)

        self.ui.button_spacing.clicked.connect(self.show_spacing_dialog)

        self.ui.action_rename.triggered.connect(self.rename_event)

        self.ui.action_find.triggered.connect(self.find_and_replace_widget.run_find_frame)
        self.ui.action_find.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_find.setShortcut(QKeySequence("Ctrl+F"))

        self.ui.action_find_and_replace.triggered.connect(self.find_and_replace_widget.run_find_and_replace_frame)
        self.ui.action_find_and_replace.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_find_and_replace.setShortcut(QKeySequence("Ctrl+Alt+F"))

        self.ui.spin_box_size.setValue(12)
        self.text_edit.setFontItalic(False)
        self.text_edit.setFontUnderline(False)
        self.text_edit.setTextColor(QColor("black"))
        self.text_edit.setFontWeight(QFont.Weight.Normal)
        self.ui.combo_box_fonts.setCurrentFont("Times New Roman")
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.set_current_color(QColor('black'))

        font = QFont("Times New Roman", 12)
        self.text_edit.setFont(font)
        self.text_edit.setFontPointSize(12)

        self.ui.combo_box_fonts.setWritingSystem(QFontDatabase.WritingSystem.Any)

        self.ui.widget_color_picker.setStyleSheet(
            "QWidget#widget_color_picker{background-color: rgb(244, 244, 244);}")

        self.update_format()
        self._update_title()
        self.update_recent_files()

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

    def resizeEvent(self, event):
        self.spacing_dialog.move(QPoint(self.size().width() // 2 - self.spacing_dialog.size().width() // 2,
                                        self.size().height() // 2 - self.spacing_dialog.size().height() // 2))

    def add_to_recent_files(self, path: str):
        add_recent_file(path)
        self.update_recent_files()

    @staticmethod
    def remove_recent_files(remove_file_path=""):
        if not remove_file_path:
            if RECENT_FILE_ACTIONS:
                for action in RECENT_FILE_ACTIONS:
                    action.deleteLater()
                RECENT_FILE_ACTIONS.clear()
        else:
            for action in RECENT_FILE_ACTIONS:
                filename = action.text()
                if remove_file_path.endswith(filename):
                    action.deleteLater()
                    RECENT_FILE_ACTIONS.remove(action)
                    remove_recent_file(remove_file_path)
                    return

    def update_recent_files(self):
        recent_files = get_info()["recent_files"]

        if not recent_files:
            return

        self.remove_recent_files()

        for path in recent_files:
            filename = QDir(path).dirName()

            new_action = QAction(self)
            new_action.setObjectName(filename)
            new_action.setText(QCoreApplication.translate("MainWindow", filename, None))

            new_action.triggered.connect(self.open_recent_file_event)

            RECENT_FILE_ACTIONS.append(new_action)
            self.ui.menuRecent.addAction(new_action)

    def delete_event(self):
        cursor = self.text_edit.textCursor()
        cursor.removeSelectedText()

    def new_file_event(self):
        if self.text_edit.toPlainText():
            if self._save_file_message() == QMessageBox.StandardButton.Cancel:
                return

        self._default_settings()
        self._update_title()

    def open_file_event(self, recent_file_path=""):
        if self.text_edit.toPlainText():
            if self._save_file_message() == QMessageBox.StandardButton.Cancel:
                return

        if not recent_file_path:
            reply = self.file_manager.open_file()
            if reply:
                self.add_to_recent_files(self.file_manager.file_path)

        else:
            self.file_manager.file_path = recent_file_path
            if not self.file_manager.open_file(is_recent_file=True):
                self._file_not_found_message()
                self.file_manager.file_path = None

                self.remove_recent_files(remove_file_path=recent_file_path)
                self.update_recent_files()
            else:
                self.add_to_recent_files(self.file_manager.file_path)

        self._update_title()

    def open_recent_file_event(self):
        recent_files = get_info()["recent_files"]
        for file in recent_files:
            if file.endswith(self.sender().text()):
                self.open_file_event(recent_file_path=file)
                return

    def save_file_event(self):
        self.file_manager.save_file()
        self._update_title()

    def rename_event(self):
        file_extension = str()
        if self.file_manager.file_path:
            if self.file_manager.file_path.find('.') != -1:
                file_extension = f".{self.file_manager.file_path.split('.')[-1]}"
        
        if self.file_manager.file_path:
            if file_extension:
                self.rename_widget.set_filename(QDir(self.file_manager.file_path).dirName()[:-len(file_extension)])
            else:
                self.rename_widget.set_filename(QDir(self.file_manager.file_path).dirName())
        else:
            self.rename_widget.set_filename("Untitled")

        if self.rename_widget.exec() == 1:
            new_filename = self.rename_widget.get_filename()

            if (self.file_manager.file_path is None) or (file_extension == ""):
                self.file_manager.file_path = new_filename.split('.')[0]
            else:
                new_filename = self.rename_widget.get_filename().split('.')[0] + file_extension
                old_filename = QDir(self.file_manager.file_path).dirName()

                directory = self.file_manager.file_path[:-len(old_filename)]
                QDir(directory).rename(old_filename, new_filename)

                self.file_manager.file_path = directory + new_filename

                for path in get_info()["recent_files"]:
                    if path == directory + old_filename:
                        self.remove_recent_files(remove_file_path=directory + old_filename)
                        self.add_to_recent_files(path=self.file_manager.file_path)
                        self.update_recent_files()

            self._update_title()

    def _update_title(self):
        self.setWindowTitle("%s - R&R Text Editor" % (QDir(self.file_manager.file_path).dirName()
                                                      if self.file_manager.file_path else "Untitled"))

    def _default_settings(self):
        self.file_manager.file_path = None
        self.text_edit.clear()

        self.ui.spin_box_size.setValue(12)
        self.text_edit.setFontItalic(False)
        self.text_edit.setFontUnderline(False)
        self.text_edit.setTextColor(QColor("black"))
        self.text_edit.setFontWeight(QFont.Weight.Normal)
        self.ui.combo_box_fonts.setCurrentFont("Times New Roman")
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.set_current_color(QColor('black'))

    @staticmethod
    def block_signals(objects, b):
        for o in objects:
            o.blockSignals(b)

    def show_spacing_dialog(self):

        for obj in self.objects_to_block:
            obj.setDisabled(True)

        self.spacing_dialog.exec()

    def close_spacing_dialog(self):

        for obj in self.objects_to_block:
            obj.setEnabled(True)

        self.spacing_dialog.hide()

    def update_format(self):
        signals = [
            self.ui.combo_box_fonts,
            self.ui.spin_box_size,
            self.ui.button_bold,
            self.ui.button_italic,
            self.ui.button_underline,
        ]

        self.block_signals(signals, True)

        self.ui.combo_box_fonts.setCurrentFont(self.text_edit.currentFont())
        self.ui.spin_box_size.setValue(int(self.text_edit.fontPointSize()))

        self.ui.button_bold.setChecked(self.text_edit.fontWeight() == QFont.Weight.Bold)
        self.ui.button_italic.setChecked(self.text_edit.fontItalic())
        self.ui.button_underline.setChecked(self.text_edit.fontUnderline())

        self.ui.button_left.setChecked(self.text_edit.alignment() == Qt.AlignmentFlag.AlignLeft)
        self.ui.button_center.setChecked(self.text_edit.alignment() == Qt.AlignmentFlag.AlignCenter)
        self.ui.button_right.setChecked(self.text_edit.alignment() == Qt.AlignmentFlag.AlignRight)
        self.ui.button_justify.setChecked(self.text_edit.alignment() == Qt.AlignmentFlag.AlignJustify)

        self.set_current_color(self.text_edit.textColor())

        self.block_signals(signals, False)

    def color_picker(self):
        color = QColorDialog.getColor()
        self.set_current_color(color)
        self.text_edit.setTextColor(color)

    def set_current_color(self, color: QColor):
        self.ui.widget_color.setStyleSheet(f"background-color: {color.name(QColor.NameFormat.HexRgb)};")

    def closeEvent(self, event):
        if not self.text_edit.toPlainText():
            event.accept()
        
        if self._save_file_message() == QMessageBox.StandardButton.Cancel:
            event.ignore()
        else:
            event.accept()
    
    def _save_file_message(self):
        reply = QMessageBox(self)
        reply.setText('Save Document')
        reply.setInformativeText('Do you want to save the current document?')
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | 
                                 QMessageBox.StandardButton.No | 
                                 QMessageBox.StandardButton.Cancel)

        result = reply.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.save_file_event()

        return result

    def _file_not_found_message(self):
        msg_box = QMessageBox(self)
        msg_box.setText('File Not Found')
        msg_box.setInformativeText('This file was not found or does not exist. Try again.')
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
