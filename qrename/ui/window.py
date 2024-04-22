# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(874, 554)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.imageDisplay = QtWidgets.QLabel(Form)
        self.imageDisplay.setMinimumSize(QtCore.QSize(160, 90))
        self.imageDisplay.setObjectName("imageDisplay")
        self.gridLayout.addWidget(self.imageDisplay, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtWidgets.QPushButton(Form)
        self.deleteButton.setMinimumSize(QtCore.QSize(60, 30))
        self.deleteButton.setMaximumSize(QtCore.QSize(60, 30))
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.itemsRemaining = QtWidgets.QLabel(Form)
        self.itemsRemaining.setMinimumSize(QtCore.QSize(120, 30))
        self.itemsRemaining.setMaximumSize(QtCore.QSize(120, 30))
        self.itemsRemaining.setObjectName("itemsRemaining")
        self.horizontalLayout.addWidget(self.itemsRemaining)
        self.loadButton = QtWidgets.QPushButton(Form)
        self.loadButton.setMinimumSize(QtCore.QSize(80, 30))
        self.loadButton.setMaximumSize(QtCore.QSize(80, 30))
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(55, 30))
        self.label_3.setMaximumSize(QtCore.QSize(55, 30))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.newName = QtWidgets.QLineEdit(Form)
        self.newName.setMinimumSize(QtCore.QSize(150, 30))
        self.newName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.newName.setObjectName("newName")
        self.horizontalLayout.addWidget(self.newName)
        self.renameButton = QtWidgets.QPushButton(Form)
        self.renameButton.setMinimumSize(QtCore.QSize(80, 30))
        self.renameButton.setMaximumSize(QtCore.QSize(80, 30))
        self.renameButton.setObjectName("renameButton")
        self.horizontalLayout.addWidget(self.renameButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qrename"))
        self.imageDisplay.setText(_translate("Form", "Load some files to get started."))
        self.deleteButton.setText(_translate("Form", "Delete File"))
        self.itemsRemaining.setText(_translate("Form", "Remaining in Queue: 500"))
        self.loadButton.setText(_translate("Form", "Load New Files"))
        self.label_3.setText(_translate("Form", "New Name:"))
        self.renameButton.setText(_translate("Form", "Rename"))
