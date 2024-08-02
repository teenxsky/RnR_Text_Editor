import os
import sys
import uuid

from PySide6.QtCore import (
    QSize,
    QEvent,
    QCoreApplication,
    QPoint,
    Signal,
    QRegularExpression,
    QDir,
    QUrl,
    QSizeF,
    QRect,
)
from PySide6.QtGui import (
    QIcon,
    Qt,
    QColor,
    QFont,
    QKeySequence,
    QAction,
    QFontDatabase,
    QImage,
    QTextDocument,
    QTextCharFormat,
    QBrush,
    QTextCursor,
    QDesktopServices,
    QTextBlockFormat,
    QPen,
    QPainter,
    QTextFrameFormat,
    QPalette,
    QGuiApplication,
    QTextListFormat,
    QTextFormat,
)
from PySide6.QtPrintSupport import (
    QPrinter,
    QPrintPreviewDialog,
    QAbstractPrintDialog,
    QPrintDialog,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QColorDialog,
    QTextEdit,
    QMessageBox,
    QDialog,
    QWidget,
    QFrame,
)

from design import Ui_MainWindow, Ui_DialogSpacing, Ui_Dialog, Ui_DialogPasteLink
from service_files import FileManager, get_info, add_recent_file, remove_recent_file

import rc.resources

RECENT_FILE_ACTIONS = []
IMAGE_EXTENSIONS = [".jpg", ".png", ".bmp"]
STYLES = [
    "Standard",
    "Bullet List (Disc)",
    "Bullet List (Circle)",
    "Bullet List (Square)",
    "Task List (Unchecked)",
    "Task List (Checked)",
    "Ordered List (Decimal)",
    "Ordered List (Alpha lower)",
    "Ordered List (Alpha upper)",
    "Ordered List (Roman lower)",
    "Ordered List (Roman upper)",
    "Heading 1",
    "Heading 2",
    "Heading 3",
    "Heading 4",
    "Heading 5",
    "Heading 6",
]


class TextEdit(QTextEdit):
    def __init__(self, size: QSize):
        super(TextEdit, self).__init__()

        self.setFixedSize(size)
        self.page_width = get_info()["PAGE_WIDTH"]
        self.page_height = get_info()["PAGE_HEIGHT"]
        self.page_top_margin = get_info()["PAGE_TOP_MARGIN"]
        self.page_bottom_margin = get_info()["PAGE_BOTTOM_MARGIN"]
        self.page_side_margin = int(size.width() - self.page_width) / 2

        self.setFrameStyle(QFrame.Shape.NoFrame)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setStyleSheet("QTextEdit { background-color: rgb(231, 231, 231); }")

        self.textChanged.connect(self.set_pages_size)

        self.frame_setup()

    def frame_setup(self):
        frame_format = QTextFrameFormat()
        frame_format.setTopMargin(self.page_top_margin + 60)
        frame_format.setLeftMargin(self.page_side_margin + 40)
        frame_format.setRightMargin(-self.page_side_margin + 40)
        frame_format.setBottomMargin(self.page_bottom_margin + 60)

        self.document().rootFrame().setFrameFormat(frame_format)

    def print_setup(self, activate: bool):
        if activate:
            self.setVisible(False)
            frame_format = QTextFrameFormat()
            frame_format.setTopMargin(self.page_top_margin + 60)
            frame_format.setBottomMargin(self.page_bottom_margin + 60)
            self.document().rootFrame().setFrameFormat(frame_format)

        else:
            self.setVisible(True)
            self.frame_setup()

    def set_pages_size(self):
        self.document().setPageSize(QSizeF(self.page_width, self.page_height))
        self.setFixedHeight(self.document().pageCount() * self.page_height)

    def setHtml(self, html: str):
        self.document().setHtml(html)
        self.frame_setup()
        self.document().setModified(False)

    def setMarkdown(self, markdown: str):
        self.document().setMarkdown(markdown)
        self.frame_setup()
        self.document().setModified(False)

    def setPlainText(self, text: str):
        self.document().setPlainText(text)
        self.frame_setup()
        self.document().setModified(False)

    def paintEvent(self, event):
        rect_painter = QPainter(self.viewport())
        rect_painter.setFont(QFont("times", 18))
        rect_painter.setBrush(QBrush(QColor("white"), Qt.BrushStyle.SolidPattern))

        for i in range(self.document().pageCount()):
            rect_painter.setPen(QPen(QColor(231, 231, 231), 1))
            rect_painter.drawRect(
                QRect(
                    int(self.page_side_margin),
                    i * self.page_height + self.page_top_margin,
                    self.page_width,
                    self.page_height - self.page_bottom_margin,
                )
            )

            rect_painter.setPen(QPen(QColor(109, 109, 109), 1))
            rect_painter.drawText(
                QPoint(
                    int(self.page_side_margin + int(self.page_width / 2)),
                    (i + 1) * self.page_height + self.page_top_margin - 63,
                ),
                str(i + 1),
            )

        super(TextEdit, self).paintEvent(event)

    def canInsertFromMimeData(self, source):

        if source.hasImage():
            return True
        else:
            return QTextEdit.canInsertFromMimeData(self, source)

    def insertFromMimeData(self, source):

        cursor = self.textCursor()
        document = self.document()

        if source.hasUrls():

            for u in source.urls():
                file_ext = os.path.splitext(str(u.toLocalFile()))[1].lower()
                if u.isLocalFile() and file_ext in IMAGE_EXTENSIONS:
                    image = QImage(u.toLocalFile())
                    document.addResource(
                        QTextDocument.ResourceType.ImageResource, u, image
                    )
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

        QTextEdit.insertFromMimeData(self, source)

    def mouseMoveEvent(self, e):
        anchor = self.anchorAt(e.pos())
        if anchor:
            QApplication.setOverrideCursor(Qt.CursorShape.PointingHandCursor)
        else:
            QApplication.setOverrideCursor(Qt.CursorShape.IBeamCursor)
        QTextEdit.mouseMoveEvent(self, e)

    def mouseReleaseEvent(self, e):
        anchor = self.anchorAt(e.pos())
        if anchor:
            QDesktopServices.openUrl(QUrl(anchor))
            QApplication.setOverrideCursor(Qt.CursorShape.IBeamCursor)
        QTextEdit.mouseReleaseEvent(self, e)


class PasteLinkDialog(Ui_DialogPasteLink, QDialog):
    cancel_clicked = Signal()
    ok_clicked = Signal()

    def __init__(self, parent: QWidget):
        super(Ui_DialogPasteLink, self).__init__()

        self.ui = Ui_DialogPasteLink()
        self.ui.setupUi(self)

        self.setParent(parent)
        self.move(
            QPoint(
                parent.size().width() // 2 - self.size().width() // 2,
                parent.size().height() // 2 - self.size().height() // 2,
            )
        )

        self.ui.button_cancel.clicked.connect(self.cancel_clicked.emit)
        self.ui.button_ok.clicked.connect(self.ok_clicked.emit)


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
        self.move(
            QPoint(
                parent.size().width() // 2 - self.size().width() // 2,
                parent.size().height() // 2 - self.size().height() // 2,
            )
        )

        self.ui.radio_min.setChecked(True)
        self.ui.check_max.setChecked(False)

        self.ui.button_cancel.clicked.connect(self.cancel_clicked.emit)
        self.ui.button_ok.clicked.connect(self.ok_clicked.emit)


class FindAndReplaceWidget:
    def __init__(self, ui: Ui_MainWindow, text_edit: QTextEdit):
        self.ui = ui
        self.ui.frame_find_and_replace.setHidden(True)

        self.ui.line_find.textChanged.connect(self.find_event)
        self.ui.button_done.clicked.connect(self.close_find_and_replace_frame)
        self.ui.button_done_2.clicked.connect(self.close_find_and_replace_frame)
        self.ui.check_regex.clicked.connect(self._set_regex_mode)
        self.ui.button_replace.clicked.connect(self.replace_event)
        self.ui.button_all.clicked.connect(self.replace_all_event)
        self.ui.button_next.clicked.connect(self._show_found_next_occurrence)
        self.ui.button_prev.clicked.connect(self._show_found_previous_occurrence)

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

    def show_find_frame(self):
        if self.ui.frame_find_and_replace.isVisible():
            self.close_find_and_replace_frame()
            return
        self.ui.frame_find_and_replace.setVisible(True)
        self.ui.frame_find.setVisible(True)
        self.ui.check_replace.setChecked(False)
        self.ui.frame_replace.setHidden(True)

    def show_find_and_replace_frame(self):
        if self.ui.frame_find_and_replace.isVisible():
            self.close_find_and_replace_frame()
            return
        self.ui.frame_find_and_replace.setVisible(True)
        self.ui.frame_find.setVisible(True)
        self.ui.check_replace.setChecked(True)
        self.ui.frame_replace.setVisible(True)

    def close_find_and_replace_frame(self):
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
            pattern = pattern.replace(".", chr(92) + ".")
            pattern = pattern.replace("*", chr(92) + "*")
            pattern = pattern.replace("?", chr(92) + "?")
            pattern = pattern.replace("+", chr(92) + "+")
            pattern = pattern.replace("^", chr(92) + "^")
            pattern = pattern.replace("$", chr(92) + "$")
            pattern = pattern.replace("(", chr(92) + "(")
            pattern = pattern.replace(")", chr(92) + "(")
            pattern = pattern.replace("[", chr(92) + "[")
            pattern = pattern.replace("]", chr(92) + "]")
            pattern = pattern.replace("{", chr(92) + "{")
            pattern = pattern.replace("}", chr(92) + "}")

        self.regex.setPattern(pattern)

        if not self.regex.isValid():
            return

        begin_index = 0
        end_index = self.regex.match(
            self.text_edit.document().toPlainText(), begin_index
        ).capturedStart()

        while end_index != -1:
            begin_index = (
                end_index
                + self.regex.match(
                    self.text_edit.document().toPlainText(), begin_index
                ).capturedLength()
            )
            self.indexes_of_occurrences.append((end_index, begin_index))
            end_index = self.regex.match(
                self.text_edit.document().toPlainText(), begin_index
            ).capturedStart()

        if len(self.indexes_of_occurrences) != 0 and show_current:
            self._show_occurrence(
                self.indexes_of_occurrences[0][0], self.indexes_of_occurrences[0][1]
            )

    def replace_event(self):
        if len(self.indexes_of_occurrences) != 0:
            self._block_show_occurrence()
            old_occurrence_index = self.current_occurrence

            self.cursor.insertText(self.ui.line_replace.text())

            self.find_event()
            self.current_occurrence = (
                old_occurrence_index - 1
                if len(self.indexes_of_occurrences) - 1 >= old_occurrence_index
                else len(self.indexes_of_occurrences) - 1
            )
            self._show_found_next_occurrence()

    def replace_all_event(self):
        self._block_show_occurrence()
        for _ in range(len(self.indexes_of_occurrences)):
            self.replace_event()

    def _show_found_previous_occurrence(self):
        self._update_current_occurrence()

        if self.current_occurrence != 0:
            self.current_occurrence -= 1
            self._show_occurrence(
                self.indexes_of_occurrences[self.current_occurrence][0],
                self.indexes_of_occurrences[self.current_occurrence][1],
            )

    def _show_found_next_occurrence(self):
        self._update_current_occurrence()

        if (
            self.current_occurrence != len(self.indexes_of_occurrences) - 1
            and self.indexes_of_occurrences != []
        ):
            self.current_occurrence += 1
            self._show_occurrence(
                self.indexes_of_occurrences[self.current_occurrence][0],
                self.indexes_of_occurrences[self.current_occurrence][1],
            )

    def _update_current_occurrence(self):
        self._block_show_occurrence()
        old_occurrence_index = self.current_occurrence
        self.find_event(show_current=False)
        self.current_occurrence = (
            old_occurrence_index
            if len(self.indexes_of_occurrences) - 1 >= old_occurrence_index
            else len(self.indexes_of_occurrences) - 1
        )
        if self.current_occurrence != -1:
            self._show_occurrence(
                self.indexes_of_occurrences[self.current_occurrence][0],
                self.indexes_of_occurrences[self.current_occurrence][1],
            )

    def _show_count_occurrences(self):
        self.ui.label_find_count.setText(
            f"""{str(self.current_occurrence + 1)}/{str(len(self.indexes_of_occurrences))}"""
        )

    def _show_occurrence(self, begin: int, end: int):
        self._block_show_occurrence()

        self.cursor.setPosition(begin, QTextCursor.MoveAnchor)
        self.cursor.setPosition(end, QTextCursor.KeepAnchor)

        self.block_format.setBackground(self.cursor.charFormat().background())
        self.block_format.setFontPointSize(self.cursor.charFormat().fontPointSize())
        self.show_format.setFontPointSize(
            self.cursor.charFormat().fontPointSize() * 1.5
        )

        self.text_edit.setTextCursor(self.cursor)
        self.text_edit.textCursor().mergeCharFormat(self.show_format)

        self._show_count_occurrences()

    def _block_show_occurrence(self):
        self.text_edit.setTextCursor(self.cursor)
        self.text_edit.textCursor().mergeCharFormat(self.block_format)
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

        self.text_edit = TextEdit(self.maximumSize())
        self.rename_widget = RenameWidget()
        self.file_manager = FileManager(self.text_edit)
        self.paste_link_dialog = PasteLinkDialog(self)
        self.spacing_dialog = SpacingDialog(self)
        self.find_and_replace_widget = FindAndReplaceWidget(self.ui, self.text_edit)

        self.spacing_pref = {
            "prop_height": self.spacing_dialog.ui.spin_prop_height.value(),
            "line_height_1": self.spacing_dialog.ui.spin_line_height_1.value(),
            "line_height_2": self.spacing_dialog.ui.spin_line_height_2.value(),
            "line_distance": self.spacing_dialog.ui.spin_line_distance.value(),
            "spacing_left": self.spacing_dialog.ui.spin_par_spacing_left.value(),
            "spacing_top": self.spacing_dialog.ui.spin_par_spacing_top.value(),
            "spacing_right": self.spacing_dialog.ui.spin_par_spacing_right.value(),
            "spacing_bottom": self.spacing_dialog.ui.spin_par_spacing_bottom.value(),
        }

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
            self.text_edit,
            self.ui.frame_tools,
            self.ui.menubar,
            self.ui.central_widget,
            self.ui.check_regex,
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

        # self.text_edit.currentCharFormatChanged.connect(self.update_format)

        self.spacing_dialog.hide()
        self.spacing_dialog.cancel_clicked.connect(self.cancel_spacing_dialog)
        self.spacing_dialog.ok_clicked.connect(self.ok_spacing_dialog)
        self.ui.frame_find_and_replace.setHidden(True)
        self.spacing_dialog.ui.spin_line_height_2.setEnabled(
            self.spacing_dialog.ui.check_max.isChecked()
        )

        self.paste_link_dialog.hide()
        self.paste_link_dialog.cancel_clicked.connect(self.close_paste_link_dialog)
        self.paste_link_dialog.ok_clicked.connect(self.paste_link)

        self.ui.widget_color_picker.installEventFilter(self)
        self.ui.widget_color_picker.setAttribute(Qt.WidgetAttribute.WA_Hover)
        self.ui.widget_color.setAutoFillBackground(True)

        self.text_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoAll)
        self.text_edit.selectionChanged.connect(self.update_format)

        self.ui.combo_box_fonts.currentFontChanged.connect(
            self.text_edit.setCurrentFont
        )
        self.ui.spin_box_size.valueChanged.connect(self.set_text_size)

        self.ui.button_left.toggled.connect(self.text_align_event)
        self.ui.button_center.toggled.connect(self.text_align_event)
        self.ui.button_right.toggled.connect(self.text_align_event)
        self.ui.button_justify.toggled.connect(self.text_align_event)

        self.ui.button_bold.toggled.connect(self.set_bold)
        self.ui.button_italic.toggled.connect(self.set_italic)
        self.ui.button_underline.toggled.connect(self.set_underline)

        self.ui.action_print.triggered.connect(self.print_file_event)
        self.ui.action_print.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_print.setShortcut(QKeySequence("Ctrl+P"))

        self.action_print_preview = QAction(self)
        self.ui.menu_file.addAction(self.action_print_preview)
        self.action_print_preview.setObjectName("action_print_preview")
        self.action_print_preview.triggered.connect(self.print_prewiev_event)
        self.action_print_preview.setText(
            QCoreApplication.translate("MainWindow", "Print Preview", None)
        )

        self.spacing_dialog.ui.spin_line_distance.valueChanged.connect(
            self.set_line_distance
        )
        self.spacing_dialog.ui.spin_line_height_1.valueChanged.connect(
            self.set_line_height
        )
        self.spacing_dialog.ui.spin_prop_height.valueChanged.connect(
            self.set_prop_height
        )
        self.spacing_dialog.ui.spin_par_spacing_left.valueChanged.connect(
            self.set_spacing_left
        )
        self.spacing_dialog.ui.spin_par_spacing_right.valueChanged.connect(
            self.set_spacing_right
        )
        self.spacing_dialog.ui.spin_par_spacing_top.valueChanged.connect(
            self.set_spacing_top
        )
        self.spacing_dialog.ui.spin_par_spacing_bottom.valueChanged.connect(
            self.set_spacing_bottom
        )

        QGuiApplication.clipboard().dataChanged.connect(self.clipboard_data_changed)

        document = self.text_edit.document()
        document.modificationChanged.connect(self.ui.action_save.setEnabled)
        document.modificationChanged.connect(self.setWindowModified)
        document.undoAvailable.connect(self.ui.action_undo.setEnabled)
        document.redoAvailable.connect(self.ui.action_redo.setEnabled)
        self.setWindowModified(document.isModified())
        self.ui.action_save.setEnabled(document.isModified())
        self.ui.action_undo.setEnabled(document.isUndoAvailable())
        self.ui.action_redo.setEnabled(document.isRedoAvailable())

        self.ui.action_cut.setEnabled(False)
        self.text_edit.copyAvailable.connect(self.ui.action_cut.setEnabled)
        self.ui.action_copy.setEnabled(False)
        self.text_edit.copyAvailable.connect(self.ui.action_copy.setEnabled)

        self.ui.combo_box_styles.addItems(STYLES)
        self.ui.combo_box_styles.activated.connect(self.set_text_style)

        # FILE ACTIONS

        self.ui.action_close.triggered.connect(self.close)
        self.ui.action_close.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_close.setPriority(QAction.Priority.LowPriority)
        self.ui.action_close.setShortcut(QKeySequence("Ctrl+W"))

        self.ui.action_new.triggered.connect(self.new_file_event)
        self.ui.action_new.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_new.setPriority(QAction.Priority.LowPriority)
        self.ui.action_new.setShortcut(QKeySequence("Ctrl+N"))

        self.ui.action_open.triggered.connect(self.open_file_event)
        self.ui.action_open.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_open.setPriority(QAction.Priority.LowPriority)
        self.ui.action_open.setShortcut(QKeySequence("Ctrl+O"))

        self.ui.action_save.triggered.connect(self.save_file_event)
        self.ui.action_save.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_save.setPriority(QAction.Priority.LowPriority)
        self.ui.action_save.setShortcut(QKeySequence("Ctrl+S"))

        # EDIT ACTIONS

        self.ui.action_cut.triggered.connect(self.text_edit.cut)
        self.ui.action_cut.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_cut.setPriority(QAction.Priority.LowPriority)
        self.ui.action_cut.setShortcut(QKeySequence("Ctrl+X"))

        self.ui.action_copy.triggered.connect(self.text_edit.copy)
        self.ui.action_copy.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_copy.setPriority(QAction.Priority.LowPriority)
        self.ui.action_copy.setShortcut(QKeySequence("Ctrl+C"))

        self.ui.action_paste.triggered.connect(self.text_edit.paste)
        self.ui.action_paste.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_paste.setPriority(QAction.Priority.LowPriority)
        self.ui.action_paste.setShortcut(QKeySequence("Ctrl+V"))

        self.ui.action_find.triggered.connect(
            self.find_and_replace_widget.show_find_frame
        )
        self.ui.action_find.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_find.setPriority(QAction.Priority.LowPriority)
        self.ui.action_find.setShortcut(QKeySequence("Ctrl+F"))

        self.ui.action_find_and_replace.triggered.connect(
            self.find_and_replace_widget.show_find_and_replace_frame
        )
        self.ui.action_find_and_replace.setShortcutContext(
            Qt.ShortcutContext.WindowShortcut
        )
        self.ui.action_find_and_replace.setPriority(QAction.Priority.LowPriority)
        self.ui.action_find_and_replace.setShortcut(QKeySequence("Ctrl+Alt+F"))

        self.ui.action_paste_link.triggered.connect(self.show_paste_link_dialog)
        self.ui.action_paste_link.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_paste_link.setPriority(QAction.Priority.LowPriority)
        self.ui.action_paste_link.setShortcut(QKeySequence("Ctrl+K"))

        self.ui.action_delete.triggered.connect(self.delete_event)
        self.ui.action_delete.setPriority(QAction.Priority.LowPriority)

        self.ui.action_undo.triggered.connect(self.text_edit.undo)
        self.ui.action_undo.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_undo.setPriority(QAction.Priority.LowPriority)
        self.ui.action_undo.setShortcut(QKeySequence.StandardKey.Undo)

        self.ui.action_redo.triggered.connect(self.text_edit.redo)
        self.ui.action_redo.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_redo.setPriority(QAction.Priority.LowPriority)
        self.ui.action_redo.setShortcut(QKeySequence.StandardKey.Redo)

        md = QGuiApplication.clipboard().mimeData()
        if md:
            self.ui.action_paste.setEnabled(md.hasText())

        # TEXT ACTIONS

        self.ui.action_bold.triggered.connect(self.set_bold)
        self.ui.action_bold.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_bold.setPriority(QAction.Priority.LowPriority)
        self.ui.action_bold.setShortcut(QKeySequence("Ctrl+B"))

        self.ui.action_italic.triggered.connect(self.set_italic)
        self.ui.action_italic.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_italic.setPriority(QAction.Priority.LowPriority)
        self.ui.action_italic.setShortcut(QKeySequence("Ctrl+I"))

        self.ui.action_underline.triggered.connect(self.set_underline)
        self.ui.action_underline.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_underline.setPriority(QAction.Priority.LowPriority)
        self.ui.action_underline.setShortcut(QKeySequence("Ctrl+U"))

        self.ui.action_left.triggered.connect(self.text_align_event)
        self.ui.action_left.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_left.setPriority(QAction.Priority.LowPriority)
        self.ui.action_left.setShortcut(QKeySequence("Ctrl+L"))

        self.ui.action_right.triggered.connect(self.text_align_event)
        self.ui.action_right.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_right.setPriority(QAction.Priority.LowPriority)
        self.ui.action_right.setShortcut(QKeySequence("Ctrl+R"))

        self.ui.action_center.triggered.connect(self.text_align_event)
        self.ui.action_center.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_center.setPriority(QAction.Priority.LowPriority)
        self.ui.action_center.setShortcut(QKeySequence("Ctrl+E"))

        self.ui.action_justify.triggered.connect(self.text_align_event)
        self.ui.action_justify.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_justify.setPriority(QAction.Priority.LowPriority)
        self.ui.action_justify.setShortcut(QKeySequence("Ctrl+J"))

        self.ui.action_indent.triggered.connect(self.indent)
        self.ui.action_indent.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_indent.setPriority(QAction.Priority.LowPriority)
        self.ui.action_indent.setShortcut(QKeySequence("Ctrl+J"))

        self.ui.action_justify.triggered.connect(self.unindent)
        self.ui.action_justify.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.ui.action_justify.setPriority(QAction.Priority.LowPriority)
        self.ui.action_justify.setShortcut(QKeySequence("Ctrl+J"))

        self.ui.button_spacing.clicked.connect(self.show_spacing_dialog)

        self.ui.action_rename.triggered.connect(self.rename_event)

        self.ui.spin_box_size.setValue(12)
        self.text_edit.setFontItalic(False)
        self.text_edit.setFontUnderline(False)
        self.text_edit.setTextColor(QColor("black"))
        self.text_edit.setFontWeight(QFont.Weight.Normal)
        self.ui.combo_box_fonts.setCurrentFont("Times New Roman")
        self.text_edit.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.set_current_color(QColor("black"))

        font = QFont("Times New Roman", 12)
        self.text_edit.setFont(font)
        self.text_edit.setFontPointSize(12)

        self.ui.combo_box_fonts.setWritingSystem(QFontDatabase.WritingSystem.Any)

        self.ui.widget_color_picker.setStyleSheet(
            "QWidget#widget_color_picker{background-color: rgb(244, 244, 244);}"
        )

        if sys.platform == "darwin":
            pal = self.text_edit.palette()
            pal.setColor(QPalette.ColorRole.Base, QColor(Qt.GlobalColor.white))
            pal.setColor(QPalette.Text, QColor(Qt.GlobalColor.black))
            self.text_edit.setPalette(pal)

        self.text_edit.setFocus()
        self._update_title()
        self.update_format()
        self.update_recent_files()

    def eventFilter(self, watched, event):
        if watched == self.ui.widget_color_picker:
            if event.type() == QEvent.Type.HoverLeave:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(244, 244, 244);}"
                )

            elif event.type() == QEvent.Type.HoverEnter:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(234, 234, 234);}"
                )

            elif event.type() == QEvent.Type.MouseButtonPress:
                self.ui.widget_color_picker.setStyleSheet(
                    "QWidget#widget_color_picker {background-color: rgb(224, 224, 224);}"
                )
                self.color_picker()

            return True

    def resizeEvent(self, event):
        self.spacing_dialog.move(
            QPoint(
                self.size().width() // 2 - self.spacing_dialog.size().width() // 2,
                self.size().height() // 2 - self.spacing_dialog.size().height() // 2,
            )
        )
        self.paste_link_dialog.move(
            QPoint(
                self.size().width() // 2 - self.spacing_dialog.size().width() // 2,
                self.size().height() // 2 - self.spacing_dialog.size().height() // 2,
            )
        )
        super(TextEditor, self).resizeEvent(event)

    def _scroll_to_cursor(self):
        new_value = self.text_edit.cursorRect().y() - (
            int((self.height() - self.ui.frame_tools.height()) / 2 + 50)
        )
        if new_value < 0:
            new_value = 0

        if (
            self.text_edit.cursorRect().y()
            > self.height()
            - self.ui.frame_tools.height()
            + self.ui.scrollArea.verticalScrollBar().value()
            - 40
        ):
            self.ui.scrollArea.verticalScrollBar().setValue(new_value)

        elif (
            self.text_edit.cursorRect().y()
            < self.ui.scrollArea.verticalScrollBar().value()
        ):
            self.ui.scrollArea.verticalScrollBar().setValue(new_value)

    def _default_text_edit_settings(self):
        self.file_manager.file_path = None
        self.file_manager.name_filter = None
        self.text_edit.setPlainText("")

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

        self.text_edit.document().setModified(False)

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
        recent_files = get_info()["RECENT_FILES"]

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

    def _save_file_message(self):
        reply = QMessageBox(self)
        reply.setText("Save Document")
        reply.setInformativeText("Do you want to save the current document?")
        reply.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
            | QMessageBox.StandardButton.Cancel
        )

        result = reply.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.save_file_event()

        return result

    def _file_not_found_message(self):
        msg_box = QMessageBox(self)
        msg_box.setText("File Not Found")
        msg_box.setInformativeText(
            "This file was not found or does not exist. Try again."
        )
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

        msg_box.exec()
        return

    def new_file_event(self):
        if self.text_edit.document().isModified():
            if self._save_file_message() == QMessageBox.StandardButton.Cancel:
                return

        self._default_text_edit_settings()
        self._update_title()

    def open_file_event(self, recent_file_path=""):
        if self.text_edit.document().isModified():
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
        recent_files = get_info()["RECENT_FILES"]
        for file in recent_files:
            if file.endswith(self.sender().text()):
                self.open_file_event(recent_file_path=file)
                return

    def save_file_event(self):
        self.file_manager.save_file()
        self._update_title()

    def print_file_event(self):
        self.text_edit.print_setup(True)

        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        print_dialog = QPrintDialog(printer, self)
        print_dialog.setWindowTitle("Print Document")

        if self.text_edit.textCursor().hasSelection():
            print_dialog.setOption(
                QAbstractPrintDialog.PrintDialogOption.PrintSelection
            )

        if print_dialog.exec() == QDialog.DialogCode.Accepted:
            self.text_edit.print_(printer)

        self.text_edit.print_setup(False)

    def print_prewiev_event(self):
        self.text_edit.print_setup(True)

        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        print_preview_dialog = QPrintPreviewDialog(printer, self)
        print_preview_dialog.paintRequested.connect(self.text_edit.print_)

        print_preview_dialog.exec()

        self.text_edit.print_setup(False)

    def text_align_event(self):
        action_name = self.sender().objectName()

        if action_name in {"button_left", "action_left"}:
            self.text_edit.setAlignment(
                Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignAbsolute
            )

        elif action_name in {"button_center", "action_center"}:
            self.text_edit.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        elif action_name in {"button_right", "action_right"}:
            self.text_edit.setAlignment(
                Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignAbsolute
            )

        elif action_name in {"button_justify", "action_justify"}:
            self.text_edit.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.text_edit.set_pages_size()

    def set_bold(self):
        if self.sender() == self.ui.action_bold:
            self.ui.button_bold.setChecked(self.ui.action_bold.isChecked())
        elif self.sender() == self.ui.button_bold:
            self.ui.action_bold.setChecked(self.ui.button_bold.isChecked())

        fmt = QTextCharFormat()
        weight = (
            QFont.Weight.Bold
            if self.ui.action_bold.isChecked()
            else QFont.Weight.Normal
        )
        fmt.setFontWeight(weight)
        self.text_edit.setFontWeight(weight)
        self.merge_format_on_word_or_selection(fmt)

    def set_italic(self):
        if self.sender() == self.ui.action_bold:
            self.ui.button_italic.setChecked(self.ui.action_italic.isChecked())
        elif self.sender() == self.ui.button_bold:
            self.ui.action_italic.setChecked(self.ui.button_italic.isChecked())

        fmt = QTextCharFormat()
        fmt.setFontItalic(self.ui.action_italic.isChecked())
        self.text_edit.setFontItalic(self.ui.action_italic.isChecked())
        self.merge_format_on_word_or_selection(fmt)

    def set_underline(self):
        if self.sender() == self.ui.action_bold:
            self.ui.button_underline.setChecked(self.ui.action_underline.isChecked())
        elif self.sender() == self.ui.button_bold:
            self.ui.action_underline.setChecked(self.ui.button_underline.isChecked())

        fmt = QTextCharFormat()
        fmt.setFontUnderline(self.ui.action_underline.isChecked())
        self.text_edit.setFontUnderline(self.ui.action_underline.isChecked())
        self.merge_format_on_word_or_selection(fmt)

    def set_text_size(self, p):
        point_size = float(p)
        fmt = QTextCharFormat()
        fmt.setFontPointSize(point_size)
        self.ui.spin_box_size.setValue(p)
        self.text_edit.setFontPointSize(p)
        self.merge_format_on_word_or_selection(fmt)

    def set_text_style(self, style_index):
        cursor = self.text_edit.textCursor()
        style = QTextListFormat.Style.ListStyleUndefined
        marker = QTextBlockFormat.MarkerType.NoMarker

        if style_index == 1:
            style = QTextListFormat.Style.ListDisc
        elif style_index == 2:
            style = QTextListFormat.Style.ListCircle
        elif style_index == 3:
            style = QTextListFormat.Style.ListSquare
        elif style_index == 4:
            if cursor.currentList():
                style = cursor.currentList().format().style()
            else:
                style = QTextListFormat.Style.ListDisc
            marker = QTextBlockFormat.MarkerType.Unchecked
        elif style_index == 5:
            if cursor.currentList():
                style = cursor.currentList().format().style()
            else:
                style = QTextListFormat.Style.ListDisc
            marker = QTextBlockFormat.MarkerType.Checked
        elif style_index == 6:
            style = QTextListFormat.Style.ListDecimal
        elif style_index == 7:
            style = QTextListFormat.Style.ListLowerAlpha
        elif style_index == 8:
            style = QTextListFormat.Style.ListUpperAlpha
        elif style_index == 9:
            style = QTextListFormat.Style.ListLowerRoman
        elif style_index == 10:
            style = QTextListFormat.Style.ListUpperRoman

        cursor.beginEditBlock()

        block_fmt = cursor.blockFormat()

        if style == QTextListFormat.Style.ListStyleUndefined:
            block_fmt.setObjectIndex(-1)
            heading_level = style_index - 11 + 1 if style_index >= 11 else 0
            block_fmt.setHeadingLevel(heading_level)
            cursor.setBlockFormat(block_fmt)

            size_adjustment = 4 - heading_level if heading_level != 0 else 0
            fmt = QTextCharFormat()
            fmt.setFontWeight(
                QFont.Weight.Bold if heading_level else QFont.Weight.Normal
            )
            fmt.setProperty(QTextFormat.Property.FontSizeAdjustment, size_adjustment)
            cursor.select(QTextCursor.LineUnderCursor)
            cursor.mergeCharFormat(fmt)
            self.text_edit.mergeCurrentCharFormat(fmt)
        else:
            block_fmt.setMarker(marker)
            cursor.setBlockFormat(block_fmt)
            list_fmt = QTextListFormat()
            if cursor.currentList():
                list_fmt = cursor.currentList().format()
            else:
                list_fmt.setIndent(block_fmt.indent() + 1)
                block_fmt.setIndent(0)
                cursor.setBlockFormat(block_fmt)
            list_fmt.setStyle(style)
            cursor.createList(list_fmt)
        cursor.endEditBlock()

    def indent(self):
        self.modify_indentation(1)

    def unindent(self):
        self.modify_indentation(-1)

    def modify_indentation(self, amount):
        cursor = self.text_edit.textCursor()
        cursor.beginEditBlock()
        if cursor.currentList():
            list_fmt = cursor.currentList().format()
            above = QTextCursor(cursor)
            above.movePosition(QTextCursor.Up)
            if (
                above.currentList()
                and list_fmt.indent() + amount == above.currentList().format().indent()
            ):
                above.currentList().add(cursor.block())
            else:
                list_fmt.setIndent(list_fmt.indent() + amount)
                cursor.createList(list_fmt)
        else:
            block_fmt = cursor.blockFormat()
            block_fmt.setIndent(block_fmt.indent() + amount)
            cursor.setBlockFormat(block_fmt)
        cursor.endEditBlock()

    def delete_event(self):
        cursor = self.text_edit.textCursor()
        cursor.removeSelectedText()

    def rename_event(self):
        file_extension = str()
        if self.file_manager.file_path:
            if self.file_manager.file_path.find(".") != -1:
                file_extension = f".{self.file_manager.file_path.split('.')[-1]}"

        if self.file_manager.file_path:
            if file_extension:
                self.rename_widget.set_filename(
                    QDir(self.file_manager.file_path).dirName()[: -len(file_extension)]
                )
            else:
                self.rename_widget.set_filename(
                    QDir(self.file_manager.file_path).dirName()
                )
        else:
            self.rename_widget.set_filename("Untitled")

        if self.rename_widget.exec() == 1:
            new_filename = self.rename_widget.get_filename()

            if (self.file_manager.file_path is None) or (file_extension == ""):
                self.file_manager.file_path = ".".join(new_filename.split(".")[:-1])
            else:
                new_filename = (
                    ".".join(self.rename_widget.get_filename().split(".")[:-1])
                    + file_extension
                )
                old_filename = QDir(self.file_manager.file_path).dirName()

                directory = self.file_manager.file_path[: -len(old_filename)]
                QDir(directory).rename(old_filename, new_filename)

                self.file_manager.file_path = directory + new_filename

                for path in get_info()["recent_files"]:
                    if path == directory + old_filename:
                        self.remove_recent_files(
                            remove_file_path=directory + old_filename
                        )
                        self.add_to_recent_files(path=self.file_manager.file_path)
                        self.update_recent_files()

            self._update_title()

    def _update_title(self):
        self.setWindowTitle(
            "%s - R&R Text Editor"
            % (
                QDir(self.file_manager.file_path).dirName()
                if self.file_manager.file_path
                else "Untitled"
            )
        )

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
        self.set_current_color(QColor("black"))

    @staticmethod
    def block_signals(objects, b):
        for o in objects:
            o.blockSignals(b)

    def show_spacing_dialog(self):

        if self.spacing_dialog.isVisible():
            self.cancel_spacing_dialog()
            return

        for obj in self.objects_to_block:
            obj.setDisabled(True)

        self.spacing_dialog.exec()

    def cancel_spacing_dialog(self):

        self.set_prop_height(self.spacing_pref["prop_height"])
        self.set_line_height(self.spacing_pref["line_height_1"])
        self.set_line_distance(self.spacing_pref["line_distance"])
        self.set_spacing_top(self.spacing_pref["spacing_top"])
        self.set_spacing_bottom(self.spacing_pref["spacing_bottom"])
        self.set_spacing_left(self.spacing_pref["spacing_left"])
        self.set_spacing_right(self.spacing_pref["spacing_right"])

        self.spacing_dialog.ui.spin_prop_height.setValue(
            self.spacing_pref["prop_height"]
        )
        self.spacing_dialog.ui.spin_line_height_1.setValue(
            self.spacing_pref["line_height_1"]
        )
        self.spacing_dialog.ui.spin_line_distance.setValue(
            self.spacing_pref["line_distance"]
        )
        self.spacing_dialog.ui.spin_par_spacing_top.setValue(
            self.spacing_pref["spacing_top"]
        )
        self.spacing_dialog.ui.spin_par_spacing_bottom.setValue(
            self.spacing_pref["spacing_bottom"]
        )
        self.spacing_dialog.ui.spin_par_spacing_left.setValue(
            self.spacing_pref["spacing_left"]
        )
        self.spacing_dialog.ui.spin_par_spacing_right.setValue(
            self.spacing_pref["spacing_right"]
        )

        for obj in self.objects_to_block:
            obj.setEnabled(True)

        self.spacing_dialog.hide()

    def ok_spacing_dialog(self):

        self.spacing_pref = {
            "prop_height": self.spacing_dialog.ui.spin_prop_height.value(),
            "line_height_1": self.spacing_dialog.ui.spin_line_height_1.value(),
            "line_height_2": self.spacing_dialog.ui.spin_line_height_2.value(),
            "line_distance": self.spacing_dialog.ui.spin_line_distance.value(),
            "spacing_left": self.spacing_dialog.ui.spin_par_spacing_left.value(),
            "spacing_top": self.spacing_dialog.ui.spin_par_spacing_top.value(),
            "spacing_right": self.spacing_dialog.ui.spin_par_spacing_right.value(),
            "spacing_bottom": self.spacing_dialog.ui.spin_par_spacing_bottom.value(),
        }

        for obj in self.objects_to_block:
            obj.setEnabled(True)

        self.spacing_dialog.hide()

    def show_paste_link_dialog(self):

        if self.paste_link_dialog.isVisible():
            self.close_paste_link_dialog()
            return

        self.paste_link_dialog.ui.lineEdit.setFocus()
        self.paste_link_dialog.ui.lineEdit.clear()

        for obj in self.objects_to_block:
            obj.setDisabled(True)

        self.paste_link_dialog.exec()

    def close_paste_link_dialog(self):

        for obj in self.objects_to_block:
            obj.setEnabled(True)

        self.paste_link_dialog.hide()

    def paste_link(self):
        cursor = self.text_edit.textCursor()
        fmt = cursor.charFormat()
        fmt.setForeground(QColor("blue"))
        fmt.setUnderlineStyle(QTextCharFormat.UnderlineStyle.SingleUnderline)
        fmt.setUnderlineColor(QColor("blue"))
        address = self.paste_link_dialog.ui.lineEdit.text()
        fmt.setAnchor(True)
        fmt.setAnchorHref(address)
        fmt.setToolTip(address)
        cursor.insertText(address, fmt)
        self.close_paste_link_dialog()

    def update_format(self):
        signals = [
            self.ui.combo_box_fonts,
            self.ui.spin_box_size,
            self.ui.button_bold,
            self.ui.button_italic,
            self.ui.button_underline,
        ]

        self.block_signals(signals, True)

        cursor_list = self.text_edit.textCursor().currentList()
        if cursor_list:
            style = cursor_list.format().style()
            if style == QTextListFormat.ListDisc:
                self.ui.combo_box_styles.setCurrentIndex(1)
            elif style == QTextListFormat.ListCircle:
                self.ui.combo_box_styles.setCurrentIndex(2)
            elif style == QTextListFormat.ListSquare:
                self.ui.combo_box_styles.setCurrentIndex(3)
            elif style == QTextListFormat.ListDecimal:
                self.ui.combo_box_styles.setCurrentIndex(6)
            elif style == QTextListFormat.ListLowerAlpha:
                self.ui.combo_box_styles.setCurrentIndex(7)
            elif style == QTextListFormat.ListUpperAlpha:
                self.ui.combo_box_styles.setCurrentIndex(8)
            elif style == QTextListFormat.ListLowerRoman:
                self.ui.combo_box_styles.setCurrentIndex(9)
            elif style == QTextListFormat.ListUpperRoman:
                self.ui.combo_box_styles.setCurrentIndex(10)
            else:
                self.ui.combo_box_styles.setCurrentIndex(-1)
        else:
            heading_level = self.text_edit.textCursor().blockFormat().headingLevel()
            new_level = heading_level + 10 if heading_level != 0 else 0
            self.ui.combo_box_styles.setCurrentIndex(new_level)

        self.ui.combo_box_fonts.setCurrentFont(self.text_edit.currentFont())
        self.ui.spin_box_size.setValue(int(self.text_edit.fontPointSize()))

        self.ui.button_bold.setChecked(self.text_edit.fontWeight() == QFont.Weight.Bold)
        self.ui.action_bold.setChecked(self.text_edit.fontWeight() == QFont.Weight.Bold)

        self.ui.button_italic.setChecked(self.text_edit.fontItalic())
        self.ui.action_italic.setChecked(self.text_edit.fontItalic())

        self.ui.button_underline.setChecked(self.text_edit.fontUnderline())
        self.ui.action_underline.setChecked(self.text_edit.fontUnderline())

        self.ui.button_left.setChecked(
            self.text_edit.alignment() == Qt.AlignmentFlag.AlignLeft
        )
        self.ui.button_center.setChecked(
            self.text_edit.alignment() == Qt.AlignmentFlag.AlignCenter
        )
        self.ui.button_right.setChecked(
            self.text_edit.alignment() == Qt.AlignmentFlag.AlignRight
        )
        self.ui.button_justify.setChecked(
            self.text_edit.alignment() == Qt.AlignmentFlag.AlignJustify
        )

        self.set_current_color(self.text_edit.textColor())

        bf = self.text_edit.textCursor().blockFormat()
        self.spacing_dialog.ui.spin_par_spacing_top.setValue(bf.topMargin())
        self.spacing_dialog.ui.spin_par_spacing_bottom.setValue(bf.bottomMargin())
        self.spacing_dialog.ui.spin_par_spacing_left.setValue(bf.leftMargin())
        self.spacing_dialog.ui.spin_par_spacing_right.setValue(bf.rightMargin())

        self.block_signals(signals, False)

    def set_line_distance(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setLineHeight(
            value, QTextBlockFormat.LineHeightTypes.LineDistanceHeight.value
        )
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_line_height(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        if self.spacing_dialog.ui.radio_fixed.isChecked():
            bf.setLineHeight(value, QTextBlockFormat.LineHeightTypes.FixedHeight.value)
        else:
            bf.setLineHeight(
                value, QTextBlockFormat.LineHeightTypes.MinimumHeight.value
            )
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_prop_height(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setLineHeight(
            value, QTextBlockFormat.LineHeightTypes.ProportionalHeight.value
        )
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_spacing_left(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setLeftMargin(value)
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_spacing_right(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setRightMargin(value)
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_spacing_top(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setTopMargin(value)
        self.text_edit.textCursor().setBlockFormat(bf)

    def set_spacing_bottom(self, value: float):
        bf = self.text_edit.textCursor().blockFormat()
        bf.setBottomMargin(value)
        self.text_edit.textCursor().setBlockFormat(bf)

    def color_picker(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return
        fmt = QTextCharFormat()
        fmt.setForeground(color)
        self.merge_format_on_word_or_selection(fmt)
        self.set_current_color(color)
        self.text_edit.setTextColor(color)

    def set_current_color(self, color: QColor):
        self.ui.widget_color.setStyleSheet(
            f"background-color: {color.name(QColor.NameFormat.HexRgb)};"
        )

    def merge_format_on_word_or_selection(self, f):
        cursor = self.text_edit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(f)
        self.text_edit.mergeCurrentCharFormat(f)

    def clipboard_data_changed(self):
        md = QGuiApplication.clipboard().mimeData()
        self.ui.action_paste.setEnabled(md and md.hasText())

    def closeEvent(self, event):
        if self.text_edit.document().isModified():
            if self._save_file_message() == QMessageBox.StandardButton.Cancel:
                event.ignore()
            else:
                event.accept()
        else:
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
