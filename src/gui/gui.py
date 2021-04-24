# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_IVS.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 460)
        MainWindow.setMinimumSize(QtCore.QSize(350, 0))
        MainWindow.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(250, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.key_4 = QtWidgets.QPushButton(self.centralwidget)
        self.key_4.setMinimumSize(QtCore.QSize(25, 80))
        self.key_4.setMaximumSize(QtCore.QSize(380, 200))
        self.key_4.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_4.setObjectName("key_4")
        self.gridLayout.addWidget(self.key_4, 3, 0, 1, 1)
        self.key_1 = QtWidgets.QPushButton(self.centralwidget)
        self.key_1.setMinimumSize(QtCore.QSize(25, 80))
        self.key_1.setMaximumSize(QtCore.QSize(380, 200))
        self.key_1.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_1.setObjectName("key_1")
        self.gridLayout.addWidget(self.key_1, 2, 0, 1, 1)
        self.key_c = QtWidgets.QPushButton(self.centralwidget)
        self.key_c.setMinimumSize(QtCore.QSize(25, 80))
        self.key_c.setMaximumSize(QtCore.QSize(380, 200))
        self.key_c.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 18pt \"Courier New\";\n" "background-color: rgb(40, 3, 77);")
        self.key_c.setObjectName("key_c")
        self.gridLayout.addWidget(self.key_c, 1, 0, 1, 1)
        self.key_mod = QtWidgets.QPushButton(self.centralwidget)
        self.key_mod.setMinimumSize(QtCore.QSize(25, 80))
        self.key_mod.setMaximumSize(QtCore.QSize(380, 200))
        self.key_mod.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_mod.setObjectName("key_mod")
        self.gridLayout.addWidget(self.key_mod, 3, 4, 1, 1)
        self.key_rand = QtWidgets.QPushButton(self.centralwidget)
        self.key_rand.setMinimumSize(QtCore.QSize(25, 80))
        self.key_rand.setMaximumSize(QtCore.QSize(380, 200))
        self.key_rand.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_rand.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.key_rand, 4, 4, 1, 1)
        self.key_fact = QtWidgets.QPushButton(self.centralwidget)
        self.key_fact.setMinimumSize(QtCore.QSize(25, 80))
        self.key_fact.setMaximumSize(QtCore.QSize(380, 200))
        self.key_fact.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_fact.setObjectName("key_fact")
        self.gridLayout.addWidget(self.key_fact, 5, 4, 1, 1)
        self.key_mul = QtWidgets.QPushButton(self.centralwidget)
        self.key_mul.setMinimumSize(QtCore.QSize(25, 80))
        self.key_mul.setMaximumSize(QtCore.QSize(380, 200))
        self.key_mul.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_mul.setObjectName("key_mul")
        self.gridLayout.addWidget(self.key_mul, 3, 3, 1, 1)
        self.key_lb = QtWidgets.QPushButton(self.centralwidget)
        self.key_lb.setMinimumSize(QtCore.QSize(25, 80))
        self.key_lb.setMaximumSize(QtCore.QSize(380, 200))
        self.key_lb.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_lb.setObjectName("key_lb")
        self.gridLayout.addWidget(self.key_lb, 1, 4, 1, 1)
        self.key_5 = QtWidgets.QPushButton(self.centralwidget)
        self.key_5.setMinimumSize(QtCore.QSize(25, 80))
        self.key_5.setMaximumSize(QtCore.QSize(380, 200))
        self.key_5.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_5.setObjectName("key_5")
        self.gridLayout.addWidget(self.key_5, 3, 1, 1, 1)
        self.key_2 = QtWidgets.QPushButton(self.centralwidget)
        self.key_2.setMinimumSize(QtCore.QSize(25, 80))
        self.key_2.setMaximumSize(QtCore.QSize(380, 200))
        self.key_2.setStyleSheet("color: rgb(241, 241, 241);\n" "selection-background-color: rgb(170, 170, 255);\n" "font: 75 16pt \"Courier New\";\n" "background-color::hover: rgb(249,96,63);")
        self.key_2.setObjectName("key_2")
        self.gridLayout.addWidget(self.key_2, 2, 1, 1, 1)
        self.key_eq = QtWidgets.QPushButton(self.centralwidget)
        self.key_eq.setMinimumSize(QtCore.QSize(50, 80))
        self.key_eq.setMaximumSize(QtCore.QSize(760, 200))
        self.key_eq.setStyleSheet("font: 13pt \"Copperplate Gothic Light\";\n" "background-color: rgb(221, 173, 78);")
        self.key_eq.setObjectName("key_eq")
        self.gridLayout.addWidget(self.key_eq, 5, 2, 1, 2)
        self.key_add = QtWidgets.QPushButton(self.centralwidget)
        self.key_add.setMinimumSize(QtCore.QSize(25, 80))
        self.key_add.setMaximumSize(QtCore.QSize(380, 200))
        self.key_add.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_add.setObjectName("key_add")
        self.gridLayout.addWidget(self.key_add, 1, 3, 1, 1)
        self.key_8 = QtWidgets.QPushButton(self.centralwidget)
        self.key_8.setMinimumSize(QtCore.QSize(25, 80))
        self.key_8.setMaximumSize(QtCore.QSize(380, 200))
        self.key_8.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_8.setObjectName("key_8")
        self.gridLayout.addWidget(self.key_8, 4, 1, 1, 1)
        self.key_point = QtWidgets.QPushButton(self.centralwidget)
        self.key_point.setMinimumSize(QtCore.QSize(25, 80))
        self.key_point.setMaximumSize(QtCore.QSize(380, 200))
        self.key_point.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_point.setObjectName("key_point")
        self.gridLayout.addWidget(self.key_point, 5, 1, 1, 1)
        self.key_sub = QtWidgets.QPushButton(self.centralwidget)
        self.key_sub.setMinimumSize(QtCore.QSize(25, 80))
        self.key_sub.setMaximumSize(QtCore.QSize(380, 200))
        self.key_sub.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_sub.setObjectName("key_sub")
        self.gridLayout.addWidget(self.key_sub, 2, 3, 1, 1)
        self.key_7 = QtWidgets.QPushButton(self.centralwidget)
        self.key_7.setMinimumSize(QtCore.QSize(25, 80))
        self.key_7.setMaximumSize(QtCore.QSize(380, 200))
        self.key_7.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_7.setObjectName("key_7")
        self.gridLayout.addWidget(self.key_7, 4, 0, 1, 1)
        self.key_3 = QtWidgets.QPushButton(self.centralwidget)
        self.key_3.setMinimumSize(QtCore.QSize(25, 80))
        self.key_3.setMaximumSize(QtCore.QSize(380, 200))
        self.key_3.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_3.setObjectName("key_3")
        self.gridLayout.addWidget(self.key_3, 2, 2, 1, 1)
        self.key_exp = QtWidgets.QPushButton(self.centralwidget)
        self.key_exp.setMinimumSize(QtCore.QSize(25, 80))
        self.key_exp.setMaximumSize(QtCore.QSize(380, 200))
        self.key_exp.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_exp.setObjectName("key_exp")
        self.gridLayout.addWidget(self.key_exp, 1, 2, 1, 1)
        self.key_div = QtWidgets.QPushButton(self.centralwidget)
        self.key_div.setMinimumSize(QtCore.QSize(25, 80))
        self.key_div.setMaximumSize(QtCore.QSize(380, 200))
        self.key_div.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_div.setObjectName("key_div")
        self.gridLayout.addWidget(self.key_div, 4, 3, 1, 1)
        self.key_9 = QtWidgets.QPushButton(self.centralwidget)
        self.key_9.setMinimumSize(QtCore.QSize(25, 80))
        self.key_9.setMaximumSize(QtCore.QSize(380, 200))
        self.key_9.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_9.setObjectName("key_9")
        self.gridLayout.addWidget(self.key_9, 4, 2, 1, 1)
        self.key_rb = QtWidgets.QPushButton(self.centralwidget)
        self.key_rb.setMinimumSize(QtCore.QSize(25, 80))
        self.key_rb.setMaximumSize(QtCore.QSize(380, 200))
        self.key_rb.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_rb.setObjectName("key_rb")
        self.gridLayout.addWidget(self.key_rb, 2, 4, 1, 1)
        self.key_0 = QtWidgets.QPushButton(self.centralwidget)
        self.key_0.setMinimumSize(QtCore.QSize(25, 80))
        self.key_0.setMaximumSize(QtCore.QSize(380, 200))
        self.key_0.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_0.setObjectName("key_0")
        self.gridLayout.addWidget(self.key_0, 5, 0, 1, 1)
        self.key_6 = QtWidgets.QPushButton(self.centralwidget)
        self.key_6.setMinimumSize(QtCore.QSize(25, 80))
        self.key_6.setMaximumSize(QtCore.QSize(380, 200))
        self.key_6.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_6.setObjectName("key_6")
        self.gridLayout.addWidget(self.key_6, 3, 2, 1, 1)
        self.key_root = QtWidgets.QPushButton(self.centralwidget)
        self.key_root.setMinimumSize(QtCore.QSize(25, 80))
        self.key_root.setMaximumSize(QtCore.QSize(380, 200))
        self.key_root.setStyleSheet("color: rgb(241, 241, 241);\n" "font: 75 16pt \"Courier New\";")
        self.key_root.setObjectName("key_root")
        self.gridLayout.addWidget(self.key_root, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(350, 60))
        self.label.setMaximumSize(QtCore.QSize(1920, 120))
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n" "background-color: rgb(19, 158, 119);\n" "font: 18pt \"Consolas\";\n" "border: 2px solid #f1f1f1;")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.key_4.setText(_translate("MainWindow", "4"))
        self.key_1.setText(_translate("MainWindow", "1"))
        self.key_c.setText(_translate("MainWindow", "C"))
        self.key_mod.setText(_translate("MainWindow", "mod"))
        self.key_rand.setText(_translate("MainWindow", "rand"))
        self.key_fact.setText(_translate("MainWindow", "!"))
        self.key_mul.setText(_translate("MainWindow", "*"))
        self.key_lb.setText(_translate("MainWindow", "("))
        self.key_5.setText(_translate("MainWindow", "5"))
        self.key_2.setText(_translate("MainWindow", "2"))
        self.key_eq.setText(_translate("MainWindow", "="))
        self.key_add.setText(_translate("MainWindow", "+"))
        self.key_8.setText(_translate("MainWindow", "8"))
        self.key_point.setText(_translate("MainWindow", ","))
        self.key_sub.setText(_translate("MainWindow", "-"))
        self.key_7.setText(_translate("MainWindow", "7"))
        self.key_3.setText(_translate("MainWindow", "3"))
        self.key_exp.setText(_translate("MainWindow", "x²"))
        self.key_div.setText(_translate("MainWindow", "/"))
        self.key_9.setText(_translate("MainWindow", "9"))
        self.key_rb.setText(_translate("MainWindow", ")"))
        self.key_0.setText(_translate("MainWindow", "0"))
        self.key_6.setText(_translate("MainWindow", "6"))
        self.key_root.setText(_translate("MainWindow", "√x"))
        self.label.setText(_translate("MainWindow", "0,000"))
