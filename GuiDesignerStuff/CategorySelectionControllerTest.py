from PyQt5 import QtCore, QtGui, uic
import sys
from PyQt5.QtWidgets import QApplication, QDialog

app = QApplication(sys.argv)
window = QDialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())



class UiWidget(QDialog):