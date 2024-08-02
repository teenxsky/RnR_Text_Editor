import os
import subprocess

import gzip
import base64

from PySide6.QtPrintSupport import QPrinter
from PySide6.QtCore import QDir, QFile, QMimeDatabase
from PySide6.QtWidgets import QFileDialog, QMainWindow, QDialog


import convertapi

convertapi.api_secret = "Okzibdk295nTMi3e"

NAME_FILTERS = [
    "Сжатый документ R&R (*.rnr)",
    "Документ Word 2007 (*.docx)",
    "Документ Word (*.doc)",
    "Документ PDF (*.pdf)",
    "Текстовый документ (*.txt *.asc *,v)",
    "Документ HTML (*.html *.htm)",
    "Документ Markdown (*.md *.mkd *.markdown)",
]


class FileManager(QMainWindow):
    def __init__(self, text_widget, *args, **kwargs) -> None:
        super(FileManager, self).__init__(*args, **kwargs)
        self.text_widget = text_widget

        self.file_path = None
        self.name_filter = None

    def open_file(self, is_recent_file=False):
        if not is_recent_file:
            file_dialog = QFileDialog(self, "Open File")

            file_dialog.setNameFilters(NAME_FILTERS)
            file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
            file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

            if file_dialog.exec() != QDialog.DialogCode.Accepted:
                return None
            else:
                self.file_path = QDir.toNativeSeparators(file_dialog.selectedFiles()[0])

        if not os.path.exists(self.file_path):
            return False

        file = QFile(self.file_path)
        file.open(QFile.OpenModeFlag.ReadOnly)
        current_mime = (
            QMimeDatabase()
            .mimeTypeForFileNameAndData(self.file_path, file.readAll())
            .name()
        )

        if current_mime == "application/gzip":
            try:
                data = open(self.file_path, "rb").read()
            except:
                return False

            data = gzip.decompress(data)
            data = base64.b64decode(data)
            self.text_widget.setHtml(data.decode()[1:-1])
            self.name_filter = "Сжатый документ R&R (*.rnr)"

        elif (
            current_mime
            == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ):
            converted_html_path = ".".join(self.file_path.split(".")[:-1]) + ".html"

            convertapi.convert(
                "html", {"File": self.file_path}, from_format="docx"
            ).save_files(
                converted_html_path[: -len(QDir(converted_html_path).dirName())]
            )

            text = open(converted_html_path, "r", encoding="utf-8").read()
            self.text_widget.setHtml(text)
            os.remove(converted_html_path)
            self.name_filter = "Документ Word 2007 (*.docx)"

        elif current_mime == "application/msword":
            converted_html_path = ".".join(self.file_path.split(".")[:-1]) + ".html"

            convertapi.convert(
                "html", {"File": self.file_path}, from_format="doc"
            ).save_files(
                converted_html_path[: -len(QDir(converted_html_path).dirName())]
            )

            text = open(converted_html_path, "r", encoding="utf-8").read()
            self.text_widget.setHtml(text)
            os.remove(converted_html_path)
            self.name_filter = "Документ Word (*.doc)"

        elif current_mime == "application/pdf":
            converted_html_path = ".".join(self.file_path.split(".")[:-1]) + ".html"

            convertapi.convert(
                "html", {"File": self.file_path}, from_format="pdf"
            ).save_files(
                converted_html_path[: -len(QDir(converted_html_path).dirName())]
            )

            text = open(converted_html_path, "r", encoding="utf-8").read()
            self.text_widget.setHtml(text)
            os.remove(converted_html_path)
            self.name_filter = "Документ PDF (*.pdf)"

        elif current_mime == "text/html":
            text = open(self.file_path, "r", encoding="utf-8").read()
            self.text_widget.setHtml(text)
            self.name_filter = "Документ HTML (*.html *.htm)"

        elif current_mime == "text/markdown":
            text = open(self.file_path, "r", encoding="utf-8").read()
            self.text_widget.setMarkdown(text)
            self.name_filter = "Документ Markdown (*.md *.mkd *.markdown)"

        else:
            text = open(self.file_path, "r", encoding="utf-8").read()
            self.text_widget.setPlainText(text)
            self.name_filter = "Текстовый документ (*.txt *.asc *,v)"

        return True

    def save_file(self):
        file_dialog = QFileDialog(self, "Save File")

        file_dialog.setNameFilters(NAME_FILTERS)
        if self.name_filter:
            file_dialog.selectNameFilter(self.name_filter)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.selectFile(
            ".".join(self.file_path.split(".")[:-1])
            if self.file_path is not None
            else "Untitled"
        )

        if file_dialog.exec() != QDialog.DialogCode.Accepted:
            return
        else:
            self.file_path = QDir.toNativeSeparators(file_dialog.selectedFiles()[0])

        selected_name_filter = file_dialog.selectedNameFilter()

        if selected_name_filter == "Текстовый документ (*.txt *.asc *,v)":
            text = self.text_widget.document().toPlainText()
            self._native_save(text)

        elif selected_name_filter == "Документ Markdown (*.md *.mkd *.markdown)":
            text = self.text_widget.document().toMarkdown()
            self._native_save(text)

        elif selected_name_filter == "Документ PDF (*.pdf)":
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(self.file_path)
            self.text_widget.document().print_(printer)

        else:
            text = self.text_widget.document().toHtml()
            if selected_name_filter == "Документ HTML (*.html *.htm)":
                self._native_save(text)

            elif selected_name_filter == "Сжатый документ R&R (*.rnr)":
                data = "[{}]".format(text).encode()
                data = base64.b64encode(data)

                with open(self.file_path, "wb") as file:
                    file.write(gzip.compress(data))

            elif (
                selected_name_filter == "Документ Word 2007 (*.docx)"
                or selected_name_filter == "Документ Word (*.doc)"
            ):

                with open(
                    ".".join(self.file_path.split(".")[:-1]) + ".html", "w"
                ) as file:
                    file.write(text)

                convertapi.convert(
                    "docx",
                    {"File": ".".join(self.file_path.split(".")[:-1]) + ".html"},
                    from_format="html",
                ).save_files(self.file_path)

                os.remove(".".join(self.file_path.split(".")[:-1]) + ".html")

            # elif selected_name_filter == 'Документ PDF (*.pdf)':
            #     with open('.'.join(self.file_path.split('.')[:-1]) + '.html', 'w') as file:
            #         file.write(text)

            #     convertapi.convert('pdf',
            #                        {'File': '.'.join(self.file_path.split('.')[:-1]) + '.html'},
            #                        from_format='html').save_files(self.file_path)

            #     os.remove('.'.join(self.file_path.split('.')[:-1]) + '.html')

        subprocess.run(["open", "-R", self.file_path])

    def _native_save(self, text: str):
        try:
            with open(self.file_path, "w") as file:
                file.write(text)
        except Exception as exc:
            print(exc)
