from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("Another Window")
        self.setFixedWidth(300)
        self.setFixedHeight(200)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("MainWindow Window")
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setWindowTitle("MainWindow Window")
        self.setFixedWidth(300)
        self.setFixedHeight(200)


    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w.close()
            self.w = None  # Discard reference.


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()