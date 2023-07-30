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

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        elif user_input.lower() in ["exit","quit"]:
            self.close()
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

    # Initialize the menu bar
    menubar = window.menuBar()
    fileMenu = QMenu("File")
    winMenu = QMenu("Window")
    helpMenu = QMenu("Help")
    menubar.addMenu(fileMenu)
    menubar.addMenu(winMenu)
    menubar.addMenu(helpMenu)
    quit_action = QAction("Exit", window)
    quit_action.triggered.connect(sys.exit)
    fileMenu.addAction(quit_action)

    msg = [
        "Welcome to Pythinux.",
        "A terminal emulator is available, and you can use it to run programs.",
        "Note that the text does not appear until the command ends.",
        "This is a known issue, and we will fix it before release.",
    ]
    msg = "\n".join(msg)
    label = QLabel(msg)
    label.setAlignment(Qt.AlignCenter)
    terminalButton = QPushButton("Launch Terminal Emulator")
    closeButton = QPushButton("Exit")
    closeButton.clicked.connect(sys.exit)
    terminalButton.clicked.connect(lambda: launchTerminal(app, currentUser))  # Simplified lambda function

    central_widget = QWidget(window)  # Set the main window as the parent for central widget

    layout = QGridLayout(central_widget)
    layout.addWidget(label, 0, 0)
    layout.addWidget(closeButton, 1, 0)

    window.setCentralWidget(central_widget)

    terminal = TerminalApp(currentUser)
    terminal.show()
    
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Perform necessary imports here (e.g., pythinux)
    startShell(currentUser)  # Call the startShell function