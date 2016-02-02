# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pipeline_order.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Pipeline_order(object):
    def setupUi(self, Pipeline_order):
        Pipeline_order.setObjectName("Pipeline_order")
        Pipeline_order.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Pipeline_order)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Pipeline_order)
        QtCore.QMetaObject.connectSlotsByName(Pipeline_order)

    def retranslateUi(self, Pipeline_order):
        _translate = QtCore.QCoreApplication.translate
        Pipeline_order.setWindowTitle(_translate("Pipeline_order", "Pipline_order"))
        self.pushButton.setText(_translate("Pipeline_order", "Add"))
        self.pushButton_3.setText(_translate("Pipeline_order", "Remove"))
        self.pushButton_2.setText(_translate("Pipeline_order", "Move Up"))
        self.pushButton_4.setText(_translate("Pipeline_order", "Move Down"))
        self.checkBox.setText(_translate("Pipeline_order", "Save Image"))

