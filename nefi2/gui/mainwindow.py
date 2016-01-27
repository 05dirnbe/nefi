import sys
from PyQt5.QtWidgets import QWidget, QStackedWidget, QApplication, QComboBox


class Window(QWidget):


    def __init__(self):
        super(Window, self).__init__()

        self.stackedWidget = QStackedWidget()
        self.orientationCombo = QComboBox()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())