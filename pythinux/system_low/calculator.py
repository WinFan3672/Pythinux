from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("Calculator")

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.base = QVBoxLayout(self.central_widget)

        self.grid = QGridLayout()
        self.frame = QFrame()
        
        self.result = 0

        self.text = QLineEdit()
        self.base.addWidget(self.text)
        
        self.menu = self.menuBar()
        self.fileMenu = QMenu("File")
        self.editMenu = QMenu("Edit")
        self.helpMenu = QMenu("Help")
        self.menu.addMenu(self.fileMenu)
        self.menu.addMenu(self.editMenu)
        self.menu.addMenu(self.helpMenu)
        
        self.exitAction = QAction("Exit")
        self.exitAction.triggered.connect(self.close)
        self.exitAction.setShortcut(QKeySequence.Quit)
        self.fileMenu.addAction(self.exitAction)
        
        self.clearAction = QAction("Clear")
        self.clearAction.triggered.connect(self.clear)
        self.clearAction.setShortcut("Esc")
        self.editMenu.addAction(self.clearAction)
        
        self.solveAction = QAction("Solve")
        self.solveAction.triggered.connect(lambda:self.button_clicked("="))
        self.solveAction.setShortcut("Return")
        self.editMenu.addAction(self.solveAction)
        
        self.buttons = [
            ["7", "8", "9", "/", "Sin(", "MS"],
            ["4", "5", "6", "*", "Cos(", "M"],
            ["1", "2", "3", "-", "Tan(", "MC"],
            ["0", ".", "C", "+", "(", ")"],
            ["Rnd", "=", "Ans", "^", "Rand", "Sqrt"],
            ["!", "pi", "e", "*10^", "Int", "Flt"],
        ]

        x, y = 0, 0
        for row in self.buttons:
            for item in row:
                b = QPushButton(item)
                b.setFixedSize(60, 40)
                function = lambda _, button=item: self.button_clicked(button)
                b.clicked.connect(function)
                self.grid.addWidget(b, x, y)
                y += 1
            x += 1
            y = 0

        self.frame.setLayout(self.grid)
        self.base.addWidget(self.frame)

        self.setLayout(self.base)
        
        self.frame.setLayout(self.grid)
        self.base.addWidget(self.frame)
    def clear(self):
        self.text.setText("")
    def button_clicked(self, button):
        button = button.replace("^","**")
        if button == "=":
            if self.text.text():
                try:
                    result = doCalc(self.text.text())
                except Exception as e:
                    result = "Error: {}".format(e)
            else:
                result = ""
            if result:
                self.result = result
            self.text.setText(str(result))
        elif button == "Ans":
            self.text.setText(str(self.result))
        else:
            t = self.text.text()
            t += button
            self.text.setText(t)


application = Calculator()        