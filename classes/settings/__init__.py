#!/usr/bin/python
import os
import sys
x = os.getcwd()
import pythinux
os.chdir(x)

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import qdarktheme
import pickle

def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()

        if widget:
            widget.setParent(None)  # Remove widget from the layout and delete it
        else:
            clearLayout(item.layout())  # Recursively clear sub-layouts

        del item  # Delete the layout item to avoid memory leaks
class GroupSettings(QWidget):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.init_ui()

    def init_ui(self):
        self.layout = QHBoxLayout()

        self.setLayout(self.layout)
        
        self.load_groups()
        self.load_settings()
    def load_groups(self):
        self.groupListBase = QGroupBox("Groups")
        self.groupConfigBase = QGroupBox("Configure")

        self.layout.addWidget(self.groupListBase)
        self.layout.addWidget(self.groupConfigBase)

        self.groupList = QVBoxLayout(self.groupListBase)
        self.groupConfig = QVBoxLayout(self.groupConfigBase)
        i = 1
        for item in pythinux.loadGroupList().list():
            group = QGroupBox("Group: {}".format(item.name))
            lay = QVBoxLayout(group)
            if item.builtin:
                    view_button = QPushButton("View Permissions")
            else:
                view_button = QPushButton("Edit Permissions")
            remove_button = QPushButton("Remove Group")
            if item.locked:
                remove_button.setEnabled(False)
            
            lay.addWidget(view_button)
            lay.addWidget(remove_button)
            self.groupList.addWidget(group)  # Fixed the layout setup here
            i += 1
        self.groupList.addStretch()
    def refresh(self):
        clearLayout(self.layout)
        self.load_groups()
        self.load_settings()
    def load_settings(self):
        self.newgroup = QGroupBox("Create Group")
        
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        
        self.groupConfig.addWidget(self.newgroup)
        self.groupConfig.addStretch()
        self.groupConfig.addWidget(self.refresh_button)
        
class UserSettings(QWidget):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.init_ui()
    def remove_user(self, user):
        cmd = "user remove '{}'".format(user.username)
        pythinux.main(self.base.currentUser,cmd)
        self.refresh()
    def init_ui(self):
        helpTopicsAction = QAction("Refresh",self)
        helpTopicsAction.triggered.connect(self.refresh)
        helpTopicsAction.setShortcut("F5")
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.init_users()
        self.init_settings()
    def create_user(self):
        u, p, g  = self.username_input.text(), self.password_input.text(), self.groupList.currentText()
        if u and p:
            cmd = "user add '{}' '{}' '{}'".format(u,p,g)
            pythinux.main(self.base.currentUser,cmd)
        self.refresh()
    def init_users(self):
        self.groupbox = QGroupBox("Users")
        self.userListBase = QVBoxLayout()
        self.frame = QFrame()
        self.userList = QVBoxLayout()
        self.groupbox.setLayout(self.userListBase)
        self.frame.setLayout(self.userList)
        self.userListBase.addWidget(self.frame)
        self.layout.addWidget(self.groupbox)
        i = 1
        for item in pythinux.loadUserList().list():
            box = QGroupBox("User #{}".format(i))
            lay = QVBoxLayout()
            box.setLayout(lay)
            msg = [
                "Username: {}".format(item.username),
                "Group: {}".format(item.group.name),
                ]
            msg = "\n".join(msg)
            label = QLabel(msg)
            label.setAlignment(Qt.AlignCenter)
            bt = QPushButton("Remove User")
            bt.clicked.connect(lambda _, user=item: self.remove_user(user))
            if not self.base.currentUser.admin():
                bt.setEnabled(False)
            lay.addWidget(label)
            lay.addWidget(bt)
            self.scrollbar = QScrollBar(Qt.Horizontal)
            self.userList.addWidget(box)
            i += 1
        self.userList.addStretch()
    def refresh(self):
        clearLayout(self.layout)
        self.init_users()
        self.init_settings()
    def autologin(self):
        cmd = "autologin '{}'".format(self.AutoLoginBox.currentText() if self.AutoLoginBox.currentText() else "--reset")
        pythinux.main(self.base.currentUser,cmd)
        self.refresh()
    def init_settings(self):
        self.generalSettings = QGroupBox("Configure Users")
        self.userSettings = QVBoxLayout()
        
        self.generalSettings.setLayout(self.userSettings)
        self.layout.addWidget(self.generalSettings)
        self.layout.setStretchFactor(self.groupbox, 1)
        self.layout.setStretchFactor(self.generalSettings, 1)
        
        self.createUserBase = QGroupBox("Create User")
        self.createUser = QVBoxLayout()
        self.createUserBase.setLayout(self.createUser)
        
        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        
        self.groupList = QComboBox()
        for item in pythinux.loadGroupList().list():
            self.groupList.addItem(item.name)
        self.groupLabel = QLabel("Select the user's group:")
        
        self.createUserButton = QPushButton("Create User")
        self.createUserButton.clicked.connect(self.create_user)
        if not self.base.currentUser.admin():
            self.createUserButton.setEnabled(False)
        
        self.createUser.addWidget(self.username_label)
        self.createUser.addWidget(self.username_input)
        self.createUser.addWidget(self.password_label)
        self.createUser.addWidget(self.password_input)
        self.createUser.addWidget(self.groupLabel)
        self.createUser.addWidget(self.groupList)
        self.createUser.addWidget(self.createUserButton)
        
        
        self.userSettings.addWidget(self.createUserBase)
        
        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.refresh)
        
        
        self.autoLoginMenu = QGroupBox("Automatic Login")
        self.autoLoginFrame = QVBoxLayout()
        self.autoLoginMenu.setLayout(self.autoLoginFrame)
        self.AutoLoginBox = QComboBox()
        self.AutoLoginBox.addItem("")
        l = [x.username for x in pythinux.loadUserList().list()]
        for i in l:
            self.AutoLoginBox.addItem(i)
        u = pythinux.loadAL()
        self.AutoLoginBox.setCurrentText(u if u else "")
        
        self.autoLoginButton = QPushButton("Set User As Default")
        self.autoLoginButton.clicked.connect(self.autologin)
        if not self.base.currentUser.admin():
            self.autoLoginButton.setEnabled(False)
        
        self.autoLoginFrame.addWidget(self.AutoLoginBox)
        self.autoLoginFrame.addWidget(self.autoLoginButton)
        
        self.userSettings.addWidget(self.autoLoginMenu)
        self.userSettings.addStretch()
        self.userSettings.addWidget(self.refreshButton)
        
    
class Setting:
    def __init__(self, title, icon_name=None, className=None):
        self.title = title
        self.icon_name = icon_name
        self.className = className


class SettingsApp(QMainWindow):
    def __init__(self,currentUser):
        super().__init__()
        self.currentUser = currentUser
        self.init_settings()
        self.init_ui()
    def init_settings(self):
        self.settings = [
                Setting("Users","user",UserSettings),
                Setting("Groups","group",GroupSettings),
            ]
    def init_ui(self):
        self.menubar = self.menuBar()
        self.fileMenu = QMenu("File")
        self.menubar.addMenu(self.fileMenu)
        self.refreshAction = QAction("Refresh")
        self.refreshAction.triggered.connect(self.refresh)
        self.refreshAction.setShortcut("F5")
        self.fileMenu.addAction(self.refreshAction)
        
        self.layout = QVBoxLayout()
        self.setWindowTitle("Pythinux Settings")
        self.setGeometry(100, 100, 800, 600)
        self.icon = QIcon("../img/settings.svg")
        self.setWindowIcon(self.icon)
        
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.load_icons()
    def refresh(self):
        clearLayout(self.layout)
        self.init_ui()
    def load_icons(self):
        x,y = 0,0
        for item in self.settings:
            if item.icon_name:
                icon = QIcon("../img/settings/{}.svg".format(item.icon_name))
            else:
                icon = QIcon("../img/settings.svg")
            if item.className:
                tabClass = item.className(self)
            else:
                tabClass = QWidget()
            self.tab_widget.addTab(tabClass, icon, item.title)