import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from PyQt5 import uic
import re
import datetime
import test
from PyQt5 import QtWebEngineWidgets, QtCore
import re
import datetime
from UI_Main import Ui_MainWindow
import sys, io
from PyQt5.QtMultimedia import QSound
import daily_chart1

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')


class Main(QMainWindow,Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자 함수 호출
        # 초기화
        self.setupUi(self)

        # 시그널 초기화
        self.initSignal()
        self.stackedWidget.setCurrentIndex(1)
        self.daily_cht = daily_chart1.daily_chart(self.view_page1)

    #     self.msg("45")
    #
    #
    # def msg(self,ms):
    #     self.home_view_1.setText("ssss"+ms)





    def initSignal(self) :
    #----- push버튼 3종세트
        # 로고/타이틀 클릭시 > 홈화면으로
        self.pushButton_logo.clicked.connect(self.changeMain_0)
        # 국내현황
        self.pushButton_local.clicked.connect(self.changeMain_1)
        self.pushButton_local.clicked.connect(self.changeCategory_0)
        self.pushButton_local.clicked.connect(self.changeView_0)
        self.pushButton_local.clicked.connect(self.show_view)

        # 세계현황
        self.pushButton_world.clicked.connect(self.changeMain_1)
        self.pushButton_world.clicked.connect(self.changeCategory_1)
        self.pushButton_world.clicked.connect(self.changeView_0)
        self.pushButton_world.clicked.connect(self.hide_view)
        # 지도
        self.pushButton_map.clicked.connect(self.changeMain_1)
        self.pushButton_map.clicked.connect(self.changeCategory_2)
        self.pushButton_map.clicked.connect(self.changeView_1)




    # 메인>뷰>체크박스 옵션 show/hide
    def show_view(self):
        self.group_view_option.show()
    def hide_view(self) :
        self.group_view_option.hide()


    # 홈/메인 전환
    def changeMain_0(self): # 홈
        self.stackedWidget.setCurrentIndex(0)
    def changeMain_1(self): # 메인
        self.stackedWidget.setCurrentIndex(1)


    # 메인> 하단 뷰창 전환
    def changeView_0(self): # 라벨
        self.main_view.setCurrentIndex(0)
    def changeView_1(self): # web뷰
        self.main_view.setCurrentIndex(1)


    # 메인 > 상단 카테고리 전환
    def changeCategory_0(self): # 국내
        self.main_category.setCurrentIndex(0)
    def changeCategory_1(self): # 세계
        self.main_category.setCurrentIndex(1)
    def changeCategory_2(self): # 지도
        self.main_category.setCurrentIndex(2)




if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
