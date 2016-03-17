import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication, QVBoxLayout)
from PyQt5.QtGui import QPixmap


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        groupOfImages = QVBoxLayout(self)
        image = QPixmap("arrow.png")

        lbl1 = QLabel(self)
        lbl1.setPixmap(image)

        lbl2 = QLabel(self)
        lbl2.setPixmap(image)

        groupOfImages.addWidget(lbl1)
        groupOfImages.addWidget(lbl2)
        self.setLayout(groupOfImages)

        self.move(300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())