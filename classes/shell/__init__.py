from PyQt5.QtWidgets import *
import os
x = os.getcwd()
import pythinux
os.chdir(x)
import sys
import subprocess
import pickle
from PyQt5.QtCore import Qt
import base64

class TerminalApp(QMainWindow):
    def __init__(self, currentUser):
        super().__init__()
        self.init_ui()
        self.currentUser = currentUser

    def init_ui(self):
        self.setWindowTitle("Terminal Emulator")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        self.input_field = QLineEdit(self)
        self.input_field.returnPressed.connect(self.process_command)
        layout.addWidget(self.input_field)

        self.setCentralWidget(central_widget)

    def process_command(self):
        user_input = self.input_field.text()
        self.input_field.clear()
        self.output_area.insertPlainText(f"{self.currentUser.group.name}@{self.currentUser.username}$ {user_input}\n")
        if user_input.lower() in ['clear', 'cls']:
            # Clear the terminal output
            self.output_area.clear()
        else:
            cmd = ["python", "-c", f"import os; os.chdir('..'); import pythinux; x = pythinux.main('{self.currentUser.uuid}','{user_input}');print(x if x else '')"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                self.output_area.insertPlainText(result.stdout.strip()+"\n")
            else:
                self.output_area.insertPlainText(result.stderr.strip()+"\n")
class Application:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
def startShell(currentUser):
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.resize(800, 600)
    window.setWindowTitle('Pythinux {} (Unstable Build)'.format(".".join([str(x) for x in pythinux.version])))        

    terminal = TerminalApp(currentUser)
    
    fileMenu = QMenu("File")
    menubar = window.menuBar()  # Get the menu bar from the QMainWindow
    menubar.addMenu(fileMenu)

    msg = [
        "Welcome to Pythinux.",
        "A terminal emulator has been loaded and you can use it to run programs.",
        "Note that the text does not appear until the command ends.",
        "This is a known issue, and we will fix it before release.",
        ]
    msg = "\n".join(msg)
    label = QLabel(msg)
    label.setAlignment(Qt.AlignCenter)
    closeButton = QPushButton("Exit")
    closeButton.clicked.connect(sys.exit)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QGridLayout(central_widget)
    layout.addWidget(label, 0, 0)
    layout.addWidget(closeButton, 1, 0)

    window.show()
    terminal.show()

    sys.exit(app.exec_())