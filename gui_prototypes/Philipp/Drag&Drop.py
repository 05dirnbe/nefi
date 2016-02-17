# from http://stackoverflow.com/questions/16210226/how-to-sort-the-items-in-qlistwidget-by-drop-and-drag

import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QListWidget, QAbstractItemView, QHBoxLayout, QPushButton, QLabel


class Widget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.widget_layout = QVBoxLayout()

        # Create ListWidget and add 10 items to move around.
        self.list_widget = QListWidget()

        self.Button = AddButton()
        self.ExampleStep1 = SingleStep("ExampleStep1")
        self.ExampleStep2 = SingleStep("ExampleStep2")

        self.list_widget.addItem(self.ExampleStep1)
        self.list_widget.addItem(self.ExampleStep2)
        self.list_widget.addItem(self.Button)

        # Enable drag & drop ordering of items.
        self.list_widget.setDragDropMode(QAbstractItemView.InternalMove)

        self.widget_layout.addWidget(self.list_widget)
        self.setLayout(self.widget_layout)


class SingleStep(QWidget):
    def __init__(self, name):
        super(SingleStep, self).__init__()

        self.widget_layout = QHBoxLayout()

        self.Name = QLabel()
        self.Name.setText(name)

        self.Button = QPushButton()
        self.Button.setText("Remove Step")

        self.widget_layout.addWidget(self.Button)
        self.setLayout(self.widget_layout)


class AddButton(QWidget):
    def __init__(self):
        super(AddButton, self).__init__()

        self.widget_layout = QVBoxLayout()

        self.Button = QPushButton()
        self.Button.setText("Add Step")

        self.widget_layout.addWidget(self.Button)
        self.setLayout(self.widget_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()

    sys.exit(app.exec_())
