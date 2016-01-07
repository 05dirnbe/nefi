# -*- coding: utf-8 -*-

import sys

from PyQt5.uic import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal


def addslider(ty):
    closed = pyqtSignal()

def buttonclick1():
    w.Label1.setText("depp")

def buttonclick2():
    w.Label1.setText("Nein")

def setselected():
    w.radioButton_2.setChecked(True)

app = QApplication(sys.argv)
w = loadUi("MainWindow.ui")

w.radioButton_2.clicked.connect(buttonclick1)
w.radioButton_1.clicked.connect(buttonclick2)


w.show()
sys.exit(app.exec_())
