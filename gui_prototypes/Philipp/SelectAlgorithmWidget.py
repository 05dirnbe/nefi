from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QGroupBox, QComboBox, QBoxLayout, QStackedWidget

from gui_prototypes.Philipp.SettingsWidget import GroupOfSliders
from gui_prototypes.Philipp.model.algorithms import algorithm_1
from gui_prototypes.Philipp.model.algorithms import algorithm_2
from gui_prototypes.Philipp.model.algorithms import category_1
from gui_prototypes.Philipp.model.algorithms import category_2


class ComboBoxWidget(QGroupBox):
    def __init__(self, name, default):
        super(ComboBoxWidget, self).__init__()

        GroupOfComboBoxesLayout = QBoxLayout(QBoxLayout.TopToBottom)
        GroupOfComboBoxesLayout.setFixedHeight(self, 300)

        for category in categories:
                GroupOfComboBoxesLayout.addWidget(ComboBox(category.get_name))

         self.setLayout(GroupOfComboBoxesLayout)


class ComboBox(QComboBox):
    def __init__(self, options):
        super(ComboBox, self).__init__()

        self.orientationCombo = QComboBox()
        self.orientationCombo.addItems(options)


class Window(QWidget):
    """
    This part can be removed for main window application
    """

    def __init__(self):
        super(Window, self).__init__()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(GroupOfSliders(MyAlgorithm))

        layout = QHBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.setWindowTitle(MyAlgorithm.get_name() + " Settings")


if __name__ == '__main__':
    import sys

    algorithms = []
    MyAlgorithm_1 = algorithm_1.MyAlgorithm_1
    MyAlgorithm_2 = algorithm_2.MyAlgorithm_2
    algorithms.append(MyAlgorithm_1)
    algorithms.append(MyAlgorithm_2)

    categories = []
    MyCategory_1 = category_1.Category()
    MyCategory_2 = category_2.Category()
    MyCategory_1.set_name("Category_1")
    MyCategory_2.set_name("Category_2")

    categories.append(MyCategory_1)
    categories.append(MyCategory_2)

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())