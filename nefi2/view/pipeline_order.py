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
        Pipeline_order.resize(250, 633)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Pipeline_order.sizePolicy().hasHeightForWidth())
        Pipeline_order.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Pipeline_order)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 251, 631))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(Pipeline_order)
        QtCore.QMetaObject.connectSlotsByName(Pipeline_order)

    def retranslateUi(self, Pipeline_order):
        _translate = QtCore.QCoreApplication.translate
        Pipeline_order.setWindowTitle(_translate("Pipeline_order", "Pipline_order"))
        self.pushButton.setText(_translate("Pipeline_order", "Add"))
        self.pushButton_2.setText(_translate("Pipeline_order", "Delete"))
        self.pushButton_3.setText(_translate("Pipeline_order", "Move Up"))
        self.pushButton_4.setText(_translate("Pipeline_order", "Move Down"))
        self.checkBox.setText(_translate("Pipeline_order", "CheckBox"))

