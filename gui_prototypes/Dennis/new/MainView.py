import PyQt5
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


base2, form2 = uic.loadUiType("NefiTemplateView2.ui")


class MainView(base2, form2):
    def __init__(self, parent=None):
        super(base2, self).__init__(parent)
        self.setupUi(self)

        pixmap = QtGui.QPixmap("wing.jpeg")
        pixmap_scaled_keeping_aspec = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio)

        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)
        self.add_cat_image("wing.jpeg", "Preprocessing", self.left_scroll_results_vbox_layout)

        self.main_image_label.setPixmap(QtGui.QPixmap("wing.jpeg"))

    def add_cat_image(self, url, image_label, parent_vbox_layout):
        """
        Creates an image item in the immediate results group
        (left side of the ui). The image will be displayed inside vertical
        layout inside a fresh widget along with its label.

        Args:
            | *url*: the url to the image
            | *image_label*: the name of the image cat e.g. preprocessing

        """
        # create top level widget and set its layout vertical
        image_vbox_layout = QtWidgets.QVBoxLayout()
        image_widget = QtWidgets.QWidget()
        image_widget.setLayout(image_vbox_layout)

        # create a pixmap and draw it into a widget with a label
        pixmap = QtGui.QPixmap(url)
        pixmap_scaled_keeping_aspec = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio)
        pixmap_widget = QtWidgets.QWidget()
        pixmap_label = QtWidgets.QLabel(pixmap_widget)
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        # create label for the image_label
        label = QtWidgets.QLabel()
        label.setText(image_label)

        # add image and label to the image_widget
        image_vbox_layout.addWidget(label)
        image_vbox_layout.addWidget(pixmap_label)

        # add the image widget to the parents vertical layout
        parent_vbox_layout.addWidget(image_widget)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    wnd2 = MainView()
    wnd2.show()

    sys.exit(app.exec_())
