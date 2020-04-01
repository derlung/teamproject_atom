# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chart_ui2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(0,0,400,500)
        Form.resize(930, 620)
        self.ScrollbarDate = QtWidgets.QScrollBar(Form)
        self.ScrollbarDate.setGeometry(QtCore.QRect(40, 580, 651, 20))
        self.ScrollbarDate.setOrientation(QtCore.Qt.Horizontal)
        self.ScrollbarDate.setObjectName("ScrollbarDate")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(740, 20, 161, 191))
        self.groupBox.setObjectName("groupBox")
        self.cb_definite = QtWidgets.QCheckBox(self.groupBox)
        self.cb_definite.resize(500,500)
        self.cb_definite.setGeometry(QtCore.QRect(40, 40, 81, 16))
        self.cb_definite.setObjectName("cb_definite")
        self.cb_treate = QtWidgets.QCheckBox(self.groupBox)
        self.cb_treate.setGeometry(QtCore.QRect(40, 70, 81, 16))
        self.cb_treate.setObjectName("cb_treate")
        self.cb_death = QtWidgets.QCheckBox(self.groupBox)
        self.cb_death.setGeometry(QtCore.QRect(40, 110, 81, 16))
        self.cb_death.setObjectName("cb_death")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(740, 230, 171, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 301))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 681, 521))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "GroupBox"))
        self.cb_definite.setText(_translate("Form", "확진자"))
        self.cb_treate.setText(_translate("Form", "완치자"))
        self.cb_death.setText(_translate("Form", "사망자"))
        self.groupBox_2.setTitle(_translate("Form", "GroupBox"))
        self.label.setText(_translate("Form", "123TextLabel1123"))
        self.label_2.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
