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
import toml

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
def getIconList():
    l = [
            {
                "name":"Terminal Emulator",
                "link":"terminal",
                "icon":False,
            }
        ]
    files = [x for x in os.listdir("icon") if x.endswith(".entry")]
    for f in files:
        with open("icon/{}".format(f)) as f:
            x = toml.loads(f.read())
            try:
                z = x["Desktop Entry"]
                _ = z["name"]
                _ = z["link"]
                _ = z["icon"]
                l.append(z)
            except:
                pass
    return l
class WindowManager:
    def __init__(self, user):
        self.windows = []
        self.app = QApplication([])
        self.user = user

    def add_window(self, window):
        if isinstance(window, QMainWindow):
            self.windows.append(window)
            window.show()
        else:
            raise ValueError("Invalid window type. Only QMainWindow is supported.")

    def remove_window(self, window):
        if window in self.windows:
            self.windows.remove(window)
            window.close()
        else:
            raise ValueError("Window not found in the window manager.")

    def run(self):
        self.app.exec_()
class TerminalApp(QMainWindow):
    def __init__(self, currentUser):
        super().__init__()
        self.init_ui()
        self.currentUser = currentUser
        self.icon = QIcon("../img/terminal.svg")
        self.setWindowIcon(self.icon)

    def init_ui(self):
        self.setWindowTitle("Terminal Emulator")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        self.cursor = self.output_area.textCursor()
        layout.addWidget(self.output_area)

        self.input_field = QLineEdit(self)
        self.input_field.returnPressed.connect(self.process_command)
        layout.addWidget(self.input_field)

        self.setCentralWidget(central_widget)

    def process_command(self):
        user_input = self.input_field.text()
        self.input_field.clear()
        self.cursor.movePosition(self.cursor.End)
        self.output_area.setTextCursor(self.cursor)
        self.output_area.insertPlainText(f"{self.currentUser.group.name}@{self.currentUser.username}$ {user_input}\n")
        if user_input.lower() in ['clear', 'cls']:
            # Clear the terminal output
            self.output_area.clear()
        elif user_input.lower() in ["exit","quit"]:
            self.close()
        else:
            cmd = ["python", "-c", f"import os; os.chdir('..'); import pythinux; x = pythinux.main('{self.currentUser.uuid}','{user_input}');print(x if x else '')"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.cursor.movePosition(self.cursor.End)
            self.output_area.setTextCursor(self.cursor)
            self.output_area.insertPlainText(result.stdout.strip()+"\n")
def loadProgram(item, currentUser, manager):
    i = pythinux.load_program(item, currentUser)
    i = i.application
    manager.add_window(i)
class ProgramLoader(QMainWindow):
    def __init__(self, user, manager):
        super().__init__()
        self.user=user
        self.manager = manager
        self.icon = QIcon("../img/progmgr.svg")
        self.setWindowIcon(self.icon)
        self.init_ui()
        self.load_icons()
    def init_ui(self):
        self.setWindowTitle("Program Loader")
        self.setGeometry(100, 100, 400, 600)

        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout(self.central_widget)

        self.setCentralWidget(self.central_widget)
    def load_icons(self):
        for item in getIconList():
            button = QPushButton(item["name"])
            button.clicked.connect(lambda:loadProgram(item["link"],self.user, self.manager))
            self.layout.addWidget(button)
    def closeEvent(self, event):
        event.ignore()
class Application:
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
def startShell(currentUser):
    manager = WindowManager(currentUser)
    window = QMainWindow()
    icon = QIcon("../img/main.svg")
    window.setWindowIcon(icon)
    window.resize(800, 600)
    window.setWindowTitle('Pythinux {} (Unstable Build)'.format(".".join([str(x) for x in pythinux.version])))

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
        "A program loader has launched.",
        "Use it to open programs, such as the built-in terminal emulator.",
        getIconList(),
    ]
    msg = "\n".join([str(x) for x in msg])
    label = QLabel(msg)
    label.setAlignment(Qt.AlignCenter)
    closeButton = QPushButton("Exit")
    closeButton.clicked.connect(sys.exit)

    central_widget = QWidget(window)  # Set the main window as the parent for central widget

    layout = QGridLayout(central_widget)
    layout.addWidget(label, 0, 0)
    layout.addWidget(closeButton, 1, 0)

    window.setCentralWidget(central_widget)
    
    # terminal = TerminalApp(currentUser)
    program_loader = ProgramLoader(currentUser, manager)
    
    # manager.add_window(terminal)
    manager.add_window(window)
    manager.add_window(program_loader)
    
    manager.run()
if __name__ == "__main__":
    # Perform necessary imports here (e.g., pythinux)
    startShell(currentUser)  # Call the startShell function