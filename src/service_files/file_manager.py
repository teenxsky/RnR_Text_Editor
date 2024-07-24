import os
import subprocess

import convertapi
import mammoth

from PySide6.QtWidgets import *
from PySide6.QtCore import QFile, QDir, QMimeDatabase

convertapi.api_secret = 'Okzibdk295nTMi3e'

MIME_TYPES = ['application/vnd.openxmlformats-officedocument.wordprocessingml.document',
              'application/msword',
              'application/pdf',
              'text/plain',
              'text/html',
              'text/markdown']


class FileManager(QMainWindow):
    def __init__(self, text_widget: QTextEdit, *args, **kwargs) -> None:
        super(FileManager, self).__init__(*args, **kwargs)
        self.text_widget = text_widget

        self.file_path = None
        self.mime_type_name = None

    def open_file(self):
        file_dialog = QFileDialog(self, "Open File")

        file_dialog.setMimeTypeFilters(MIME_TYPES)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec() != QDialog.DialogCode.Accepted:
            return
        else:
            self.file_path = QDir.toNativeSeparators(file_dialog.selectedFiles()[0])

        file = QFile(self.file_path)
        file.open(QFile.OpenModeFlag.ReadOnly)
        self.mime_type_name = QMimeDatabase().mimeTypeForFileNameAndData(self.file_path, file.readAll()).name()

        if self.mime_type_name == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            with open(self.file_path, 'rb') as docx_file:
                result = mammoth.convert_to_html(docx_file)
                self.text_widget.setHtml(result.value)

        elif self.mime_type_name == 'application/msword':
            converted_html_path = self.file_path[:-4] + '.html'
            convertapi.convert('html',
                               {'File': self.file_path},
                               from_format='doc').save_files(
                converted_html_path[:-len(converted_html_path.split('/')[-1])])
            text = open(converted_html_path, 'r', encoding='utf-8').read()
            self.text_widget.setHtml(text)
            os.remove(converted_html_path)

        elif self.mime_type_name == 'application/pdf':
            converted_html_path = self.file_path[:-4] + '.html'
            convertapi.convert('html',
                               {'File': self.file_path},
                               from_format='pdf').save_files(
                converted_html_path[:-len(converted_html_path.split('/')[-1])])
            text = open(converted_html_path, 'r', encoding='utf-8').read()
            self.text_widget.setHtml(text)
            os.remove(converted_html_path)

        elif self.mime_type_name == 'text/html':
            text = open(self.file_path, 'r', encoding='utf-8').read()
            self.text_widget.setHtml(text)

        elif self.mime_type_name == 'text/markdown':
            text = open(self.file_path, 'r', encoding='utf-8').read()
            self.text_widget.setMarkdown(text)

        else:
            text = open(self.file_path, 'r', encoding='utf-8').read()
            self.text_widget.setPlainText(text)

    def save_file(self):
        file_dialog = QFileDialog(self, "Save File")

        file_dialog.setDefaultSuffix("odt")
        file_dialog.setMimeTypeFilters(MIME_TYPES)
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.selectFile(self.file_path if self.file_path is not None else "Untitled")

        if file_dialog.exec() != QDialog.DialogCode.Accepted:
            return
        else:
            self.file_path = QDir.toNativeSeparators(file_dialog.selectedFiles()[0])

        selected_mime_type = file_dialog.selectedMimeTypeFilter()

        if selected_mime_type == 'text/plain':
            text = self.text_widget.toPlainText()
            self._apply_save(text)

        elif selected_mime_type == 'text/markdown':
            text = self.text_widget.toMarkdown()
            self._apply_save(text)

        else:
            text = self.text_widget.toHtml()
            if selected_mime_type == 'text/html':
                self._apply_save(text)

            elif selected_mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                with open(self.file_path[:-5] + '.html', 'w') as file:
                    file.write(text)
                convertapi.convert('docx',
                                   {'File': self.file_path[:-5] + '.html'},
                                   from_format='html').save_files(self.file_path)
                os.remove(self.file_path[:-5] + '.html')

            elif selected_mime_type == 'application/msword':
                with open(self.file_path[:-4] + '.html', 'w') as file:
                    file.write(text)
                convertapi.convert('docx',
                                   {'File': self.file_path[:-4] + '.html'},
                                   from_format='html').save_files(self.file_path)
                os.remove(self.file_path[:-4] + '.html')

            elif selected_mime_type == 'application/pdf':
                with open(self.file_path[:-4] + '.html', 'w') as file:
                    file.write(text)
                convertapi.convert('pdf',
                                   {'File': self.file_path[:-4] + '.html'},
                                   from_format='html').save_files(self.file_path)
                os.remove(self.file_path[:-4] + '.html')

        # subprocess.Popen(['open', self.file_path 
        #                           if os.path.isdir(self.file_path) 
        #                           else os.path.dirname(self.file_path)])
        subprocess.run(["open", "-R", self.file_path])

    def _apply_save(self, text: str):
        try:
            with open(self.file_path, 'w') as file:
                file.write(text)
        except Exception as exc:
            print(exc)
