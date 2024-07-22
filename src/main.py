import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication

from design import Ui_MainWindow

import rc.resources


class TextEditor(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__set_icons_svg()

    def __set_icons_svg(self):

        # Calcite Sharp Line Icons Collection
        # https://www.svgrepo.com/collection/calcite-sharp-line-icons/14

        icon_left = QIcon()
        icon_left.addFile(":icons/icons/left.svg", QSize(), QIcon.Normal)
        self.ui.button_left.setIcon(icon_left)
        self.ui.button_left.setIconSize(QSize(17, 17))

        icon_center = QIcon()
        icon_center.addFile(":icons/icons/center.svg", QSize(), QIcon.Normal)
        self.ui.button_center.setIcon(icon_center)
        self.ui.button_center.setIconSize(QSize(17, 17))

        icon_right = QIcon()
        icon_right.addFile(":icons/icons/right.svg", QSize(), QIcon.Normal)
        self.ui.button_right.setIcon(icon_right)
        self.ui.button_right.setIconSize(QSize(17, 17))

        icon_justify = QIcon()
        icon_justify.addFile(":icons/icons/justify.svg", QSize(), QIcon.Normal)
        self.ui.button_justify.setIcon(icon_justify)
        self.ui.button_justify.setIconSize(QSize(17, 17))

        icon_intervals = QIcon()
        icon_intervals.addFile(":icons/icons/intervals.svg", QSize(), QIcon.Normal)
        self.ui.button_intervals.setIcon(icon_intervals)
        self.ui.button_intervals.setIconSize(QSize(17, 17))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec())
