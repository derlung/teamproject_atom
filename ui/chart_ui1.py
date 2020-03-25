# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 20, 601, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.checkBox = QtWidgets.QCheckBox(self.page)
        self.checkBox.setGeometry(QtCore.QRect(500, 50, 81, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 80, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page)
        self.checkBox_3.setGeometry(QtCore.QRect(500, 110, 81, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.page)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(20, 430, 411, 16))
        self.horizontalScrollBar.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.horizontalScrollBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalScrollBar.setProperty("value", 0)
        self.horizontalScrollBar.setSliderPosition(0)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(self.page_2)
        self.horizontalScrollBar_2.setGeometry(QtCore.QRect(70, 410, 411, 16))
        self.horizontalScrollBar_2.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.horizontalScrollBar_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalScrollBar_2.setProperty("value", 0)
        self.horizontalScrollBar_2.setSliderPosition(0)
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_4.setGeometry(QtCore.QRect(490, 120, 81, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_5.setGeometry(QtCore.QRect(490, 160, 81, 16))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.page_2)
        self.checkBox_6.setGeometry(QtCore.QRect(490, 80, 81, 16))
        self.checkBox_6.setObjectName("checkBox_6")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 110, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "확진자"))
        self.checkBox_2.setText(_translate("MainWindow", "완치자"))
        self.checkBox_3.setText(_translate("MainWindow", "사망자"))
        self.checkBox_4.setText(_translate("MainWindow", "완치자"))
        self.checkBox_5.setText(_translate("MainWindow", "사망자"))
        self.checkBox_6.setText(_translate("MainWindow", "확진자"))
        self.pushButton.setText(_translate("MainWindow", "일일"))
        self.pushButton_2.setText(_translate("MainWindow", "누적"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
