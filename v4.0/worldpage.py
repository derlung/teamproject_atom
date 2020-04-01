# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(751, 700)
        self.nation = QtWidgets.QLabel(Form)
        self.nation.setGeometry(QtCore.QRect(450, 455, 171, 21))
        self.nation.setObjectName("nation")
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setGeometry(QtCore.QRect(380, 450, 41, 31))
        self.searchButton.setObjectName("searchButton")
        self.definite = QtWidgets.QLabel(Form)
        self.definite.setGeometry(QtCore.QRect(600, 455, 201, 21))
        self.definite.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.definite.setObjectName("definite")
        self.background = QtWidgets.QLabel(Form)
        self.background.setGeometry(QtCore.QRect(490, 350, 150, 150))
        self.background.setObjectName("background")
        self.nationInput = QtWidgets.QLineEdit(Form)
        self.nationInput.setGeometry(QtCore.QRect(0, 450, 371, 31))
        self.nationInput.setObjectName("nationInput")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nation.setText(_translate("Form", "nations"))
        self.searchButton.setText(_translate("Form", "검색"))
        self.definite.setText(_translate("Form", "definite"))
        self.background.setText(_translate("Form", "background"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
