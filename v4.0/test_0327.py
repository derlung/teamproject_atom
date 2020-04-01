# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sk0327.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 681)
        self.background_img=QtWidgets.QLabel(Form)
        self.background_img.setGeometry(QtCore.QRect(0,-55, 1221, 791))
        self.background_img.setText("")
        self.background_img.setPixmap(QtGui.QPixmap("D:/teamproject/project_atom1_git/teamproject_atom/v2.1/img_source/chart_layout.jpg"))
        self.background_img.setObjectName("background_img")
        self.ScrollbarDate = QtWidgets.QScrollBar(Form)
        self.ScrollbarDate.setGeometry(QtCore.QRect(200, 646, 561, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScrollbarDate.sizePolicy().hasHeightForWidth())
        self.ScrollbarDate.setSizePolicy(sizePolicy)
        self.ScrollbarDate.setOrientation(QtCore.Qt.Horizontal)
        self.ScrollbarDate.setObjectName("ScrollbarDate")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 181, 651))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("날짜 디테일 정보")
        self.la_totaldef = QtWidgets.QLabel(self.groupBox)
        self.la_totaldef.setGeometry(QtCore.QRect(20, 500, 121, 21))
        self.la_totaldef.setObjectName("la_totaldef")
        self.la_totaldeth = QtWidgets.QLabel(self.groupBox)
        self.la_totaldeth.setGeometry(QtCore.QRect(20, 590, 121, 21))
        self.la_totaldeth.setObjectName("la_totaldeth")
        self.la_totaltre = QtWidgets.QLabel(self.groupBox)
        self.la_totaltre.setGeometry(QtCore.QRect(20, 550, 121, 21))
        self.la_totaltre.setObjectName("la_totaltre")
        self.la_dailydeth = QtWidgets.QLabel(self.groupBox)
        self.la_dailydeth.setGeometry(QtCore.QRect(30, 340, 81, 21))
        self.la_dailydeth.setObjectName("la_dailydeth")
        self.la_dailydef = QtWidgets.QLabel(self.groupBox)
        self.la_dailydef.setGeometry(QtCore.QRect(30, 260, 81, 21))
        self.la_dailydef.setObjectName("la_dailydef")
        self.la_dailytre = QtWidgets.QLabel(self.groupBox)
        self.la_dailytre.setGeometry(QtCore.QRect(30, 300, 81, 21))
        self.la_dailytre.setObjectName("la_dailytre")
        self.cb_treate = QtWidgets.QCheckBox(self.groupBox)
        self.cb_treate.setGeometry(QtCore.QRect(50, 140, 81, 16))
        self.cb_treate.setObjectName("cb_treate")
        self.cb_definite = QtWidgets.QCheckBox(self.groupBox)
        self.cb_definite.setGeometry(QtCore.QRect(50, 60, 81, 16))
        self.cb_definite.setObjectName("cb_definite")
        self.cb_death = QtWidgets.QCheckBox(self.groupBox)
        self.cb_death.setGeometry(QtCore.QRect(50, 100, 81, 16))
        self.cb_death.setObjectName("cb_death")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.la_totaldef.setText(_translate("Form", "<font color='red'>누적확진자</font>"))
        self.la_totaldeth.setText(_translate("Form", "누적사망자"))
        self.la_totaltre.setText(_translate("Form", "누적완치자"))
        self.la_dailydeth.setText(_translate("Form", "사망자"))
        self.la_dailydef.setText(_translate("Form", "확진자"))
        self.la_dailytre.setText(_translate("Form", "완치자"))
        self.cb_treate.setText(_translate("Form", "완치자"))
        self.cb_definite.setText(_translate("Form", "확진자"))
        self.cb_death.setText(_translate("Form", "사망자"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
