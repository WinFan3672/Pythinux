x = os.getcwd()
import pythinux
os.chdir(x)

pkm = pythinux.load_library("pkm",currentUser)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Upgrade(QDialog):
    def __init__(self):
        super().__init__()
        self.layoutBase = QVBoxLayout()  # Define layoutBase
        self.layout = QVBoxLayout(self.layoutBase)
        self.setLayout(self.layoutBase)
        self.init_upgrades()  # Call init_upgrades before init_ui

    def init_ui(self):
        self.groupbox = QGroupBox()
        self.scrollArea = QScrollArea(self.groupbox)
        self.upgradeLayout = QVBoxLayout(self.scrollArea)

        self.refreshButton = QPushButton("Reload")
        self.refreshButton.clicked.connect(self.refresh)
        self.loadLabel = QLabel()

        self.layout.addWidget(self.groupbox)
        self.layout.addStretch()
        self.layout.addWidget(self.refreshButton)

        print(self.upgrades)

    def init_upgrades(self):
        print(1)
        apps = pkm.list_app()
        print(2)
        infs = pkm.loadPackageInfs()
        print(3)
        dbs = pkm.give_dbs(True)
        print(4)
        self.upgrades = []
        for item in apps:
            print(item)
            if dbs[item]["version"] > infs[item]["version"]:
                self.upgrades.append(item)

        # Process pending events to ensure UI updates before continuing
        QCoreApplication.processEvents()

    def refresh(self):
        classes.settings.clearLayout(self.layout)  # Make sure you complete this line with the necessary code
        self.init_upgrades()
        self.init_ui()
class Upgrade(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.init_ui()
    def init_ui(self):
        self.group = QGroupBox("Install Updates")
        self.layout.addWidget(self.group)
        self.layout.addStretch()
        self.refreshButton = QPushButton("Reload Page")
        self.refreshButton.clicked.connect(self.refresh)
        self.layout.addWidget(self.refreshButton)
    def refresh(self):
        pass
class Databases(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.init_ui()
    def init_ui(self):
        self.dbListBase= QGroupBox("Databases")
        self.frame = QFrame()
        self.configBatch = QVBoxLayout()
        self.frame.setLayout(self.configBatch)
        self.configBase = QGroupBox("Create Database")
        
        
        self.dbList = QVBoxLayout(self.dbListBase)
        self.config = QVBoxLayout(self.configBase)
        
        self.layout.addWidget(self.dbListBase)
        self.configBatch.addWidget(self.configBase)
        self.layout.addWidget(self.frame)
        
        for item in pkm.update_db():
            box = QGroupBox(item)
            lay = QVBoxLayout(box)
            button = QPushButton("Remove")
            button.clicked.connect(lambda _,item=item: self.remove(item))
            lay.addWidget(button)
            self.dbList.addWidget(box)
        self.dbList.addStretch()
        
        self.nameLabel = QLabel("Name of Database:")
        self.nameInput = QLineEdit()
        self.urlLabel = QLabel("URL:")
        self.urlInput = QLineEdit()
        self.button = QPushButton("Add Database")
        self.button.clicked.connect(self.add_database)
        
        self.config.addWidget(self.nameLabel)
        self.config.addWidget(self.nameInput)
        self.config.addWidget(self.urlLabel)
        self.config.addWidget(self.urlInput)
        self.config.addWidget(self.button)
        
        self.configBatch.addStretch()
        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.refresh)
        self.configBatch.addWidget(self.refreshButton)
    def remove(self, item):
        db = pkm.update_db()
        db.pop(item)
        pkm.save_db(db)
        self.refresh()
    def add_database(self):
        name, url = self.nameInput.text(), self.urlInput.text()
        if name and url:
            db = pkm.update_db()
            db[name] = url
            pkm.save_db(db)
        self.refresh()
    def refresh(self):
        classes.settings.clearLayout(self.layout)
        self.init_ui()
class Home(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Welcome to Software Centre.",alignment = Qt.AlignCenter)
        self.layout.addWidget(self.label)
class Tab:
    def __init__(self, name, tab):
        self.name = name
        self.tab = tab

class SoftwareCenter(QMainWindow):
    def __init__(self, currentUser):
        super().__init__()
        self.icon = QIcon("../img/softwarecenter.svg")
        self.setWindowIcon(self.icon)
        self.user = currentUser
        self.setWindowTitle("Software Centre")
        self.setGeometry(100, 100, 800, 600)
        self.init_tabs()
        self.init_ui()

    def init_tabs(self):
        self.tab_items = [
            Tab("Home", Home),
            Tab("Upgrade",Upgrade),
            Tab("Databases",Databases),
        ]

    def init_ui(self):
        self.central = QWidget(self)
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)
        for item in self.tab_items:
            tabClass = item.tab()
            self.tabs.addTab(tabClass, item.name)
application = SoftwareCenter(currentUser)