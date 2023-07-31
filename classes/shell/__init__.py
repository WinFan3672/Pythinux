from PyQt5.QtWidgets import *
import os
import time

x = os.getcwd()
import pythinux
os.chdir(x)

import sys
import subprocess
import pickle
from PyQt5.QtCore import Qt
import base64
import toml
import traceback

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarktheme
import markdown
def getIconList():
    l = [
            {
                "name":"Terminal Emulator",
                "link":"terminal",
                "icon":"terminal",
            },
            {
                "name":"Help Topics",
                "link":"guihelp",
                "icon":"guihelp",
            },
        ]
    files = [x for x in os.listdir("icon") if x.endswith(".entry")]
    for f in files:
        with open("icon/{}".format(f)) as f:
            x = toml.loads(f.read())
            try:
                z = x["Desktop Entry"]
                _, _, _ = z["name"], z["link"], z["icon"]
                l.append(z)
            except:
                pass
    return l
class WindowManager:
    def __init__(self, user):
        self.windows = []
        self.app = QApplication([])
        qdarktheme.setup_theme()
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
    try:
        i = pythinux.load_program(item, currentUser)
        i = i.application
        manager.add_window(i)
    except:
        print(traceback.format_exc())
class HelpTopicsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        icon = QIcon("../img/guihelp.svg")
        self.setWindowIcon(icon)
        self.setWindowTitle('Pythinux {}: Help Topics'.format(".".join([str(x) for x in pythinux.version])))
        self.setGeometry(100, 100, 800, 600)

        # Create a QFileSystemModel to populate the tree view
        self.model = QFileSystemModel()
        self.model.setRootPath('')  # Set an initial path
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        # Specify the path to the help topics folder
        help_topics_folder = '../helptopics'
        root_index = self.model.index(help_topics_folder)
        if root_index.isValid():
            self.model.setRootPath(self.model.filePath(root_index))
            self.tree_view = QTreeView(self)
            self.tree_view.setModel(self.model)
            self.tree_view.setRootIndex(root_index)

            # Hide the unnecessary size, type, and date fields from the header
            header = self.tree_view.header()
            header.setSectionHidden(1, True)  # Size column
            header.setSectionHidden(2, True)  # Type column
            header.setSectionHidden(3, True)  # Date column

            # Create a QTextBrowser widget to display the help topics content
            self.text_browser = QTextBrowser()

            # Create a layout to arrange the tree view and text browser vertically
            layout = QHBoxLayout()
            layout.addWidget(self.tree_view)
            layout.addWidget(self.text_browser)

            # Create a central widget and set the layout
            central_widget = QWidget()
            central_widget.setLayout(layout)
            self.setCentralWidget(central_widget)

            # Connect the item selection signal to show_help_content method
            self.tree_view.selectionModel().selectionChanged.connect(self.show_help_content)
        else:
            print(f"Invalid root index: {help_topics_folder}")

    def show_help_content(self, selected, deselected):
        # Get the path of the selected item
        indexes = selected.indexes()
        if indexes:
            index = indexes[0]
            path = self.model.filePath(index)

            # Check if the selected item is a file
            if self.model.isDir(index):
                # Clear the QTextBrowser if a directory is selected
                self.text_browser.setPlainText('')
            else:
                # Read the content of the selected help topic file and display it in the QTextBrowser
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    html_content = markdown.markdown(content)
                    self.text_browser.setHtml(html_content)
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
        
        self.menubar = self.menuBar()
        self.fileMenu = QMenu("File")
        self.menubar.addMenu(self.fileMenu)
        self.refresh_action = QAction("Refresh", self)
        self.refresh_action.setShortcut("F5")
        self.refresh_action.triggered.connect(self.refresh)
        self.fileMenu.addAction(self.refresh_action)
        
        self.central_widget = QWidget(self)
        self.layout = QGridLayout(self.central_widget)

        self.setCentralWidget(self.central_widget)
    def load_icons(self):
        icons = []
        for item in getIconList():
            if item["icon"]:
                if isinstance(item["icon"],str):
                    icon = QIcon("../img/{}.svg".format(item["icon"]))
                else:
                    icon = QIcon("icon/{}.svg".format(item["name"]))
            else:
                icon = QIcon("../img/default.svg")
            action = QAction("Load", self)
            action.triggered.connect(lambda _, link=item["link"]: loadProgram(link, self.user, self.manager))
            icons.append((icon, action, item))

        x, y = 0, 0
        for icon, action, item in icons:
            button = QToolButton()
            button.setIcon(icon)
            button.setIconSize(QSize(64, 64))
            button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            button.setText(item["name"])
            button.clicked.connect(action.triggered)
            self.layout.addWidget(button, x, y)
            y += 1
            if y >= 5:
                x += 1
                y = 0
    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                clear_layout(item.layout())
    def refresh(self):
        self.clear_layout()
        print("Did Refresh")
        self.load_icons()
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
    helpTopicsAction = QAction("Help Topics",window)
    helpTopicsAction.triggered.connect(lambda:loadProgram("guihelp",currentUser,manager))
    quit_action = QAction("Exit", window)
    quit_action.triggered.connect(sys.exit)
    fileMenu.addAction(quit_action)

    msg = [
        "Welcome to Pythinux.",
        "This is the central window.",
        "If this window closes, everything does.",
        "A program manager has also launched.",
        "It allows you to launch programs.",
        "For help, go to Help > Help Topics."
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