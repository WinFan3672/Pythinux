#!/usr/bin/python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox, QFontComboBox
from PyQt5.QtGui import QIcon, QTextCursor, QTextCharFormat, QFont

class WordProcessor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        self.init_menu_bar()
        self.init_format_bar()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Word Processor")
        self.show()

    def init_menu_bar(self):
        new_action = QAction(QIcon(), "New", self)
        new_action.triggered.connect(self.new_file)

        open_action = QAction(QIcon(), "Open", self)
        open_action.triggered.connect(self.open_file)

        save_action = QAction(QIcon(), "Save", self)
        save_action.triggered.connect(self.save_file)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

    def init_format_bar(self):
        font_combo = QFontComboBox(self)
        font_combo.currentFontChanged.connect(self.set_text_font)

        self.format_bar = self.addToolBar("Format")
        self.format_bar.addWidget(font_combo)

    def set_text_font(self, font):
        format = QTextCharFormat()
        format.setFont(font)
        cursor = self.text_edit.textCursor()
        cursor.mergeCharFormat(format)
        self.text_edit.mergeCurrentCharFormat(format)

    def new_file(self):
        self.text_edit.clear()

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "r") as file:
                self.text_edit.setPlainText(file.read())

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            with open(file_name, "w") as file:
                file.write(self.text_edit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WordProcessor()
    sys.exit(app.exec_())
