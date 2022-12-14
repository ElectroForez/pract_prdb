# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/personalAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(419, 466)
        MainWindow.setMaximumSize(QtCore.QSize(419, 466))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font-weight: bold;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.photo_label = QtWidgets.QLabel(self.centralwidget)
        self.photo_label.setMaximumSize(QtCore.QSize(150, 150))
        self.photo_label.setText("")
        self.photo_label.setPixmap(QtGui.QPixmap("design/../../res/Вариант 9/Сессия 1/Сотрудники_import/Иванов.jpeg"))
        self.photo_label.setScaledContents(True)
        self.photo_label.setObjectName("photo_label")
        self.horizontalLayout.addWidget(self.photo_label)
        self.mainLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.fio_label = QtWidgets.QLabel(self.centralwidget)
        self.fio_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fio_label.setObjectName("fio_label")
        self.horizontalLayout_2.addWidget(self.fio_label)
        self.mainLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.position_label = QtWidgets.QLabel(self.centralwidget)
        self.position_label.setAlignment(QtCore.Qt.AlignCenter)
        self.position_label.setObjectName("position_label")
        self.horizontalLayout_3.addWidget(self.position_label)
        self.mainLayout.addLayout(self.horizontalLayout_3)
        self.see_history = QtWidgets.QPushButton(self.centralwidget)
        self.see_history.setObjectName("see_history")
        self.mainLayout.addWidget(self.see_history)
        self.create_order_btn = QtWidgets.QPushButton(self.centralwidget)
        self.create_order_btn.setObjectName("create_order_btn")
        self.mainLayout.addWidget(self.create_order_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 419, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.deauth_btn = QtWidgets.QAction(MainWindow)
        self.deauth_btn.setObjectName("deauth_btn")
        self.exit_btn = QtWidgets.QAction(MainWindow)
        self.exit_btn.setObjectName("exit_btn")
        self.menu.addSeparator()
        self.menu.addAction(self.deauth_btn)
        self.menu.addAction(self.exit_btn)
        self.menubar.addAction(self.menu.menuAction())
        self.label_2.setBuddy(self.label_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Личный Кабинет"))
        self.label_2.setText(_translate("MainWindow", "Личный кабинет"))
        self.label_4.setText(_translate("MainWindow", "ФИО:"))
        self.fio_label.setText(_translate("MainWindow", "Значение"))
        self.label_5.setText(_translate("MainWindow", "Должность"))
        self.position_label.setText(_translate("MainWindow", "Значение"))
        self.see_history.setText(_translate("MainWindow", "Посмотреть историю входа"))
        self.create_order_btn.setText(_translate("MainWindow", "Создать заказ"))
        self.menu.setTitle(_translate("MainWindow", "Аккаунт"))
        self.deauth_btn.setText(_translate("MainWindow", "Деавторизация"))
        self.deauth_btn.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.exit_btn.setText(_translate("MainWindow", "Закрыть"))
        self.exit_btn.setShortcut(_translate("MainWindow", "Ctrl+W"))
