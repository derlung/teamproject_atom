# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_0327.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

    # ★★★★★★★★★★★★★★★ 이미지 저장 경로 변경★★★★★★★★★★★★★★★★★★★
        save="D:/teamproject/project_atom1_git/teamproject_atom/v3.0/img_source/"
    # ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★



        # 전체배경
        self.background_img = QtWidgets.QLabel(self.centralwidget)
        self.background_img.setGeometry(QtCore.QRect(10, 10, 1221, 791))
        self.background_img.setText("")
        self.background_img.setPixmap(QtGui.QPixmap(save+"background.jpg"))
        self.background_img.setObjectName("background_img")


        # stackedWidget_홈/메인
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(420, 0, 781, 771))
        self.stackedWidget.setObjectName("stackedWidget")

        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")


        # 홈 - 확진자현황
        self.group_condition = QtWidgets.QGroupBox(self.home)
        self.group_condition.setGeometry(QtCore.QRect(0, 0, 791, 261))
        self.group_condition.setTitle("")
        self.group_condition.setObjectName("group_condition")
            # 확진자현황-img
        self.label_condition_img = QtWidgets.QLabel(self.group_condition)
        self.label_condition_img.setGeometry(QtCore.QRect(10, 0, 771, 271))
        # self.label_condition_img.setStyleSheet("font: 30pt \"돋움\";")
        self.label_condition_img.setAutoFillBackground(True)
        self.label_condition_img.setPixmap(QtGui.QPixmap(save+"label_condition_img.jpg"))
        self.label_condition_img.setObjectName("label_condition_img")

        self.label_con_1 = QtWidgets.QLabel(self.group_condition)
        #라벨위치바꿈 ()
        self.label_con_1.setGeometry(QtCore.QRect(270, 20, 61, 31))
        self.label_con_1.setStyleSheet("font: 20pt \"돋움\";")
        self.label_con_1.setObjectName("label_con_1")

        self.label_con_2 = QtWidgets.QLabel(self.group_condition)
        self.label_con_2.setGeometry(QtCore.QRect(660, 20, 71, 31))
        self.label_con_2.setStyleSheet("font: 20pt \"돋움\";")
        self.label_con_2.setObjectName("label_con_2")

        #라벨위치바꿈
        self.label_con_3 = QtWidgets.QLabel(self.group_condition)
        self.label_con_3.setGeometry(QtCore.QRect(60, 110, 121, 101))
        self.label_con_3.setStyleSheet("font: 30pt \"돋움\";")
        self.label_con_3.setObjectName("label_con_3")

        self.label_con_4 = QtWidgets.QLabel(self.group_condition)
        self.label_con_4.setGeometry(QtCore.QRect(260, 110, 121, 101))
        self.label_con_4.setStyleSheet("font: 30pt \"돋움\";")
        self.label_con_4.setObjectName("label_con_4")

        self.label_con_5 = QtWidgets.QLabel(self.group_condition)
        self.label_con_5.setGeometry(QtCore.QRect(460, 110, 131, 101))
        self.label_con_5.setStyleSheet("font: 30pt \"돋움\";")
        self.label_con_5.setObjectName("label_con_5")

        self.label_con_6 = QtWidgets.QLabel(self.group_condition)
        self.label_con_6.setGeometry(QtCore.QRect(650, 110, 101, 101))
        self.label_con_6.setStyleSheet("font: 30pt \"돋움\";")
        self.label_con_6.setObjectName("label_con_6")

        self.label_con_7 = QtWidgets.QLabel(self.group_condition)
        self.label_con_7.setGeometry(QtCore.QRect(120, 200, 111, 51))
        self.label_con_7.setObjectName("label_con_7")

        self.label_con_8 = QtWidgets.QLabel(self.group_condition)
        self.label_con_8.setGeometry(QtCore.QRect(300, 200, 111, 51))
        self.label_con_8.setObjectName("label_con_8")

        self.label_con_9 = QtWidgets.QLabel(self.group_condition)
        self.label_con_9.setGeometry(QtCore.QRect(510, 200, 111, 51))
        self.label_con_9.setObjectName("label_con_9")

        self.label_con_10 = QtWidgets.QLabel(self.group_condition)
        self.label_con_10.setGeometry(QtCore.QRect(680, 200, 71, 51))
        self.label_con_10.setObjectName("label_con_10")

        # 홈 - 개요/예방수칙
        self.group_view = QtWidgets.QGroupBox(self.home)
        self.group_view.setGeometry(QtCore.QRect(0, 280, 781, 481))
        self.group_view.setTitle("")
        self.group_view.setObjectName("group_view")
            # 개요
        self.home_view_1 = QtWidgets.QLabel(self.group_view)
        self.home_view_1.setGeometry(QtCore.QRect(40, 40, 711, 151))
        self.home_view_1.setStyleSheet("font: 30pt \"돋움\";")
        self.home_view_1.setObjectName("home_view_1")
            # 예방수칙
        self.home_view_2 = QtWidgets.QLabel(self.group_view)
        self.home_view_2.setGeometry(QtCore.QRect(40, 260, 711, 151))
        self.home_view_2.setStyleSheet("font: 30pt \"돋움\";")
        self.home_view_2.setObjectName("home_view_2")





        #-- 메인 stackedWidget 시작
        self.stackedWidget.addWidget(self.home)
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")

        # 메인-뷰3개
        self.main_category = QtWidgets.QStackedWidget(self.main)
        self.main_category.setGeometry(QtCore.QRect(0, 0, 1000, 770))
        self.main_category.setObjectName("main_category")
            # 로컬
        self.page_local = QtWidgets.QWidget()
        self.page_local.setObjectName("page_local")
        self.group_category_local = QtWidgets.QGroupBox(self.page_local)
        self.group_category_local.setGeometry(QtCore.QRect(0, 10, 781, 71))
        self.group_category_local.setTitle("")
        self.group_category_local.setObjectName("group_category_local")

        self.label_local_img = QtWidgets.QLabel(self.group_category_local)
        self.label_local_img.setGeometry(QtCore.QRect(10, 10, 771, 41))
        # self.label_local_img.setStyleSheet("font: 30pt \"돋움\";")
        self.label_local_img.setPixmap(QtGui.QPixmap(save+"category_local.jpg"))
        self.label_local_img.setObjectName("label_local_img")


        self.pushButton_category_local_1 = QtWidgets.QPushButton(self.group_category_local)
        self.pushButton_category_local_1.setGeometry(QtCore.QRect(10, 10, 141, 51))
        self.pushButton_category_local_1.setFlat(True)
        self.pushButton_category_local_1.setObjectName("pushButton_category_local_1")
        self.pushButton_category_local_2 = QtWidgets.QPushButton(self.group_category_local)
        self.pushButton_category_local_2.setGeometry(QtCore.QRect(190, 10, 141, 51))
        self.pushButton_category_local_2.setFlat(True)
        self.pushButton_category_local_2.setObjectName("pushButton_category_local_2")
        self.pushButton_category_local_3 = QtWidgets.QPushButton(self.group_category_local)
        self.pushButton_category_local_3.setGeometry(QtCore.QRect(370, 10, 141, 51))
        self.pushButton_category_local_3.setFlat(True)
        self.pushButton_category_local_3.setObjectName("pushButton_category_local_3")

            # 로컬> 뷰페이지
        self.stackedWidget_local_view = QtWidgets.QStackedWidget(self.page_local)
        self.stackedWidget_local_view.setGeometry(QtCore.QRect(20, 90, 760, 680))
        self.stackedWidget_local_view.setObjectName("stackedWidget_local_view")
            # 뷰1
        self.view_daily_chart = QtWidgets.QWidget()
        self.view_daily_chart.setObjectName("view_daily_chart")
        self.label_local_view_1 = QtWidgets.QLabel(self.view_daily_chart)
        self.label_local_view_1.setGeometry(QtCore.QRect(220, 130, 56, 12))
        self.label_local_view_1.setObjectName("label_local_view_1")
        self.stackedWidget_local_view.addWidget(self.view_daily_chart)
            # 뷰2
        self.view_total_chart = QtWidgets.QWidget()
        self.view_total_chart.setObjectName("view_total_chart")
        self.label_local_view_2 = QtWidgets.QLabel(self.view_total_chart)
        self.label_local_view_2.setGeometry(QtCore.QRect(260, 280, 56, 12))
        self.label_local_view_2.setObjectName("label_local_view_2")
        self.stackedWidget_local_view.addWidget(self.view_total_chart)
            # 뷰3
        self.page_local_view_3 = QtWidgets.QWidget()
        self.page_local_view_3.setObjectName("page_local_view_3")
        self.label_local_view_3 = QtWidgets.QLabel(self.page_local_view_3)
        self.label_local_view_3.setGeometry(QtCore.QRect(220, 260, 56, 12))
        self.label_local_view_3.setObjectName("label_local_view_3")
        self.stackedWidget_local_view.addWidget(self.page_local_view_3)

        self.main_category.addWidget(self.page_local)   #-- 로컬 끝



            # 세계
        self.page_world = QtWidgets.QWidget()
        self.page_world.setObjectName("page_world")
        self.group_category_world = QtWidgets.QGroupBox(self.page_world)
        self.group_category_world.setGeometry(QtCore.QRect(0, 10, 781, 71))
        self.group_category_world.setTitle("")
        self.group_category_world.setObjectName("group_category_world")
        self.label_world_img = QtWidgets.QLabel(self.group_category_world)
        self.label_world_img.setGeometry(QtCore.QRect(10, 10, 771, 41))
        # self.label_world_img.setStyleSheet("font: 30pt \"돋움\";")
        self.label_world_img.setPixmap(QtGui.QPixmap(save+"category_world.jpg"))
        self.label_world_img.setObjectName("label_world_img")
        self.pushButton_category_world = QtWidgets.QPushButton(self.group_category_world)
        self.pushButton_category_world.setGeometry(QtCore.QRect(20, 10, 171, 51))
        self.pushButton_category_world.setFlat(True)
        self.pushButton_category_world.setObjectName("pushButton_category_world")

        self.label_world_view = QtWidgets.QLabel(self.page_world)
        self.label_world_view.setGeometry(QtCore.QRect(20, 90, 751, 651))
            # 세계 뷰
        self.label_world_view.setObjectName("label_world_view")
        self.main_category.addWidget(self.page_world)



            # 지도
        self.page_map = QtWidgets.QWidget()
        self.page_map.setObjectName("page_map")
        self.group_category_map = QtWidgets.QGroupBox(self.page_map)
        self.group_category_map.setGeometry(QtCore.QRect(0, 10, 781, 71))
        self.group_category_map.setTitle("")
        self.group_category_map.setObjectName("group_category_map")
        self.label_map_img = QtWidgets.QLabel(self.group_category_map)
        self.label_map_img.setGeometry(QtCore.QRect(10, 10, 771, 41))
        # self.label_map_img.setStyleSheet("font: 30pt \"돋움\";")
        self.label_map_img.setPixmap(QtGui.QPixmap(save+"category_map.jpg"))
        self.label_map_img.setObjectName("label_map_img")

        self.pushButton_category_map = QtWidgets.QPushButton(self.group_category_map)
        self.pushButton_category_map.setGeometry(QtCore.QRect(20, 10, 171, 51))
        self.pushButton_category_map.setFlat(True)
        self.pushButton_category_map.setObjectName("pushButton_category_map")
                # 지도 뷰 (웹뷰)
        self.webEngine_map_view = QtWebEngineWidgets.QWebEngineView(self.page_map)
        self.webEngine_map_view.setGeometry(QtCore.QRect(10, 90, 721, 661))
        self.webEngine_map_view.setUrl(QtCore.QUrl("about:blank"))
        self.webEngine_map_view.setObjectName("webEngine_map_view")
        self.main_category.addWidget(self.page_map)


        self.stackedWidget.addWidget(self.main) # -- 메인 위젯 끝

        # 제일 큰 푸쉬버튼들

        self.group_pushButton = QtWidgets.QGroupBox(self.centralwidget)
        self.group_pushButton.setGeometry(QtCore.QRect(10, 10, 411, 771))
        self.group_pushButton.setTitle("")
        self.group_pushButton.setObjectName("group_pushButton")
            # 국내현황 푸쉬버튼
        self.pushButton_local = QtWidgets.QPushButton(self.group_pushButton)
        self.pushButton_local.setGeometry(QtCore.QRect(10, 170, 391, 191))
                # ---이미지
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(save+"pushbutton_local.jpg"))
        self.pushButton_local.setIcon(icon)
        self.pushButton_local.setIconSize(QtCore.QSize(390,300))
        self.pushButton_local.setObjectName("pushButton_local")


            # 세계현황 푸쉬버튼
        self.pushButton_world = QtWidgets.QPushButton(self.group_pushButton)
        self.pushButton_world.setGeometry(QtCore.QRect(10, 375, 391, 191))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(save+"pushButton_world.jpg"))
        self.pushButton_world.setIcon(icon)
        self.pushButton_world.setIconSize(QtCore.QSize(390,300))
        self.pushButton_world.setObjectName("pushButton_world")
            # 지도 푸쉬버튼
        self.pushButton_map = QtWidgets.QPushButton(self.group_pushButton)
        self.pushButton_map.setGeometry(QtCore.QRect(10, 580, 391, 191))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(save+"pushButton_map.jpg"))
        self.pushButton_map.setIcon(icon)
        self.pushButton_map.setIconSize(QtCore.QSize(390,300))
        self.pushButton_map.setObjectName("pushButton_map")
            # 로고/타이틀 푸쉬버튼
        self.pushButton_logo = QtWidgets.QPushButton(self.group_pushButton)
        self.pushButton_logo.setGeometry(QtCore.QRect(10, 20, 391, 131))
        # self.pushButton_logo.setStyleSheet("font: 30pt \"돋움\";")
        # self.pushButton_logo.setAutoDefault(False)
        # self.pushButton_logo.setDefault(False)
        self.pushButton_logo.setFlat(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(save+"logo_img.png"))
        self.pushButton_logo.setIcon(icon)
        self.pushButton_logo.setIconSize(QtCore.QSize(390,300))
        self.pushButton_logo.setObjectName("pushButton_logo")




        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1273, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")


        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.main_category.setCurrentIndex(0)
        self.stackedWidget_local_view.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        # self.label_condition_img.setText(_translate("MainWindow", "확진자 현황_이미지들어갈곳"))
        self.label_con_1.setText(_translate("MainWindow", "일확"))
        self.label_con_2.setText(_translate("MainWindow", "일확"))
        self.label_con_3.setText(_translate("MainWindow", "확진자"))
        self.label_con_6.setText(_translate("MainWindow", "완치자"))
        self.label_con_4.setText(_translate("MainWindow", "치료중"))
        self.label_con_5.setText(_translate("MainWindow", "사망"))
        self.label_con_7.setText(_translate("MainWindow", "전일대비"))
        self.label_con_8.setText(_translate("MainWindow", "전일대비"))
        self.label_con_9.setText(_translate("MainWindow", "전일대비"))
        self.label_con_10.setText(_translate("MainWindow", "전일대비"))
        self.home_view_1.setText(_translate("MainWindow", "개요"))
        self.home_view_2.setText(_translate("MainWindow", "예방수칙"))
        # self.labe_local_img.setText(_translate("MainWindow", "카테고리(국내현황)"))
        # self.pushButton_category_local_1.setText(_translate("MainWindow", "일별"))
        # self.pushButton_category_local_2.setText(_translate("MainWindow", "누적"))
        # self.pushButton_category_local_3.setText(_translate("MainWindow", "치사율"))
        self.label_local_view_1.setText(_translate("MainWindow", "국내 뷰 1"))
        self.label_local_view_2.setText(_translate("MainWindow", "국내뷰2"))
        self.label_local_view_3.setText(_translate("MainWindow", "국내뷰3"))
        # self.label_world_img.setText(_translate("MainWindow", "카테고리(해외현황)"))
        # self.pushButton_category_world.setText(_translate("MainWindow", "나라별 통계"))
        self.label_world_view.setText(_translate("MainWindow", "해외 뷰"))
        # self.label_map_img.setText(_translate("MainWindow", "카테고리(지도)"))
        self.pushButton_category_map.setText(_translate("MainWindow", "map"))

        # self.pushButton_local.setText(_translate("MainWindow", "국내현황"))
        # self.pushButton_world.setText(_translate("MainWindow", "해외현황"))
        # self.pushButton_map.setText(_translate("MainWindow", "지도보기"))
        # self.pushButton_logo.setText(_translate("MainWindow", "로고/타이틀"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
