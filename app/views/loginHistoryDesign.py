# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/loginHistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(610, 406)
        Form.setMinimumSize(QtCore.QSize(610, 406))
        Form.setMaximumSize(QtCore.QSize(921, 652))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.history_table = QtWidgets.QTableWidget(Form)
        self.history_table.setObjectName("history_table")
        self.history_table.setColumnCount(3)
        self.history_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.history_table)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "История входа"))
        item = self.history_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "New Column"))
        item = self.history_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "New Column"))
        item = self.history_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "New Column"))
