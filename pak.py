# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaK.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(10, 10, 75, 25))
        self.btn_open.setObjectName("btn_open")

        self._btn_print = QtWidgets.QPushButton(self.centralwidget)
        self._btn_print.setGeometry(QtCore.QRect(95, 10, 75, 25))
        self._btn_print.setObjectName("_btn_print")

        self.table_main = QtWidgets.QTableWidget(self.centralwidget)
        self.table_main.setGeometry(QtCore.QRect(10, 80, 1170, 700))
        self.table_main.setObjectName("table_main")
        self.table_main.resizeColumnsToContents()

        self.ward_one = QtWidgets.QCheckBox(self.centralwidget)
        self.ward_one.setGeometry(QtCore.QRect(10, 50, 50, 17))
        self.ward_one.setObjectName("ward_one")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def add_ward(w):
            for i in w:
                self. = QtWidgets.QCheckBox(self.centralwidget)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open.setText(_translate("MainWindow", "Открыть"))
        self._btn_print.setText(_translate("MainWindow", "Печать"))
        self.ward_one.setText(_translate("MainWindow", "2222"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())