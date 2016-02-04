from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import qdarkstyle

class RightControlbarController():
    def __init__(self):
        pass

class SceneGraphModel(QtCore.QAbstractItemModel):
    def __init__(self):
        self.setu

        pass

base2, form2 = uic.loadUiType("NefiTemplateView.ui")
base1, form1 = uic.loadUiType("RightControlBar.ui")
base3, form3 = uic.loadUiType("ImageShowWidget.ui")
base4, form4 = uic.loadUiType("LeftWidget.ui")
base5, form5 = uic.loadUiType("MainWindow.ui")

class MainView(base5, form5):
    def __init__(self, parent=None):
        super(base5, self).__init__(parent)
        self.setupUi(self)

        pixmap = QtGui.QPixmap("wing.jpeg")
        pixmap_scaled_keeping_aspec = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio)

        widget1 = QtWidgets.QWidget(self)
        widget2 = QtWidgets.QWidget(self)
        widget3 = QtWidgets.QWidget(self)
        widget4 = QtWidgets.QWidget(self)

        QtWidgets.QLabel(widget1).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget2).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget3).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget4).setPixmap(pixmap_scaled_keeping_aspec)

        intermediat_layout = self.intermediate_results

        self.intermediat_layout.addWidget(widget1)
        self.intermediat_layout.addWidget(widget2)
        self.intermediat_layout.addWidget(widget3)
        self.intermediat_layout.addWidget(widget4)

        """
        CentralView.\
        main_layout.\
        center_display_group.\
        center_scroll.\
        main_image_widget.\
        """

        self.main_image.setPixmap(QtGui.QPixmap("wing.jpeg"))

"""
class TemplateView(base2, form2):
    def __init__(self, parent=None):
        super(base2, self).__init__(parent)
        self.setupUi(self)
        self.horizontalLayout.addWiget
        self.left= LeftWidget(self)
        self.middle = ImageShowWidget(self)
        self.right = RightControlWidget(self)



        #self.RightControlWidget = RightControlWidget(self)
        #self.ImageShowWidget =


class RightControlWidget(base1, form1):
    def __init__(self, parent=None):
        super(base1, self).__init__(parent)
        self.setupUi(self)


class LeftWidget(base4, form4):
    def __init__(self, parent=None):
        super(base4, self).__init__(parent)
        self.setupUi(self)

        pixmap = QtGui.QPixmap("wing.jpeg")
        pixmap_scaled_keeping_aspec = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio)


        #self.listWidget.addItem(pixmap_scaled_keeping_aspec)
        #self.listWidget.addItem(pixmap_scaled_keeping_aspec)
        #self.listWidget.addItem(pixmap_scaled_keeping_aspec)
        #self.listWidget.addItem(pixmap_scaled_keeping_aspec)

        widget1 = QtWidgets.QWidget(self)
        widget2 = QtWidgets.QWidget(self)
        widget3 = QtWidgets.QWidget(self)
        widget4 = QtWidgets.QWidget(self)

        QtWidgets.QLabel(widget1).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget2).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget3).setPixmap(pixmap_scaled_keeping_aspec)
        QtWidgets.QLabel(widget4).setPixmap(pixmap_scaled_keeping_aspec)

        self.verticalLayout.addWidget(widget1)
        self.verticalLayout.addWidget(widget2)
        self.verticalLayout.addWidget(widget3)
        self.verticalLayout.addWidget(widget4)


class ImageShowWidget(base3, form3):
    def __init__(self, parent=None):
        super(base3, self).__init__(parent)
        self.setupUi(self)

        #pic = QtWidgets.QLabel(self)
        #pic.setGeometry(10, 10, 400, 100)

        self.main_image.setPixmap(QtGui.QPixmap("wing.jpeg"))

"""

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    #wnd = RightControlBar()
    #wnd.show()

    wnd2 = MainView()
    wnd2.show()

    #wnd3 = ImageShowWidget()
    #wnd3.show()

    sys.exit(app.exec_())
