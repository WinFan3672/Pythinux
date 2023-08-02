x = os.getcwd()
import pythinux
os.chdir(x)

pkm = pythinux.load_library("pkm",currentUser)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Manage(QDialog):
    def __init__(self):
        super().__init__()
        self.base = QVBoxLayout(self)
        self.setLayout(self.base)
        self.didInit = False
        
        self.init_ui()
        self.init_list()
    def init_ui(self):
        self.layout = QVBoxLayout()
        self.frame=QFrame()
        self.frame.setLayout(self.layout)
        self.base.addWidget(self.frame)
        self.splitter = QSplitter(Qt.Horizontal)  # Create a horizontal splitter

        self.listBase = QGroupBox("Program List")
        self.listLayout = QVBoxLayout(self.listBase)

        self.configBase = QGroupBox("Configuration")

        self.splitter.addWidget(self.listBase)
        self.splitter.addWidget(self.configBase)

        self.splitter.setSizes([1, 1])  # Equal sizes for both widgets
        self.layout.addWidget(self.splitter)
        
        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.refresh)
        self.layout.addWidget(self.refreshButton)
        
        self.didInit = True

    def init_list(self):
        self.combo = QComboBox()
        
        for item in pkm.list_app():
            self.combo.addItem(item)
            
        self.selectLabel = QLabel("Select Program")
        self.infoButton = QPushButton("View Program Info")
        self.removeButton = QPushButton("Remove Program")
        
        self.listLayout.addWidget(self.selectLabel)
        self.listLayout.addWidget(self.combo)
        self.listLayout.addWidget(self.infoButton)
        self.listLayout.addWidget(self.removeButton)
        
        self.listLayout.addStretch()
    def clear_layout(self):
        while self.base.count():
            item = self.base.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    def refresh(self):
        self.clear_layout()
        self.init_ui()
        self.init_list()
class UpdatingScreen(QSplashScreen):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        loading = QLabel("Updates are being installed.\nThis may take a while.")
        layout.addWidget(loading, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)
        self.centerOnScreen()

    def centerOnScreen(self):
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        loading = QLabel("Loading...")
        layout.addWidget(loading, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)

        pixmap = QPixmap("../img/splash/softwarecenter.png")
        self.setPixmap(pixmap)

        self.centerOnScreen()

    def centerOnScreen(self):
        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

class Update(QDialog):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.init_upgrades()
        self.init_ui()

    def init_ui(self):
        self.refreshButton = QPushButton("Reload")
        self.refreshButton.clicked.connect(self.refresh)
        self.loadLabel = QLabel()
        if self.upgrades:
            if len(self.upgrades) == 1:
                label = QLabel("1 update is ready to be installed.")
            else:
                label = QLabel("{} updates are ready to be installed.".format(len(self.upgrades)))
            button = QPushButton("Install Updates")
            button.clicked.connect(self.upgrade)
            self.layout.addWidget(label)
            self.layout.addWidget(button)
        else:
            label = QLabel("No updates to install.")
            self.layout.addWidget(label)
        self.layout.addStretch()
        self.layout.addWidget(self.refreshButton)
    def clear_layout(self):
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    def upgrade(self):
        cmd = "pkm upgrade"
        s = UpdatingScreen()
        s.show()
        main(currentUser,"pkm upgrade")
        s.close()
        self.refresh()
    def init_upgrades(self):
        apps = pkm.list_app()
        infs = pkm.loadPackageInfs()
        dbs = pkm.give_dbs(True,True)
        self.upgrades = []
        for item in apps:
            if dbs[item]["version"] > infs[item]["version"]:
                self.upgrades.append(item)

        # Process pending events to ensure UI updates before continuing
        QCoreApplication.processEvents()

    def refresh(self):
        self.clear_layout()
        self.init_upgrades()
        self.init_ui()
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
        self.setFixedSize(800, 600)
        self.setGeometry(100, 100, 800, 600)
        self.init_tabs()
        self.init_ui()

    def init_tabs(self):
        self.tab_items = [
            Tab("Updates",Update),
            Tab("Manage",Manage),
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
splash = SplashScreen()
splash.show()
application = SoftwareCenter(currentUser)
splash.finish(application)