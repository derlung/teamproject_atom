import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import re
import datetime
import test
import re
import datetime
from UI_Main import Ui_MainWindow
import sys, io
from PyQt5.QtMultimedia import QSound
#차트 import
import daily_chart1
import total_chart1
import world_bar as w_b
import bar
import pie

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
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_local_view.setCurrentIndex(0)

        #차트 붙이기
        self.chart1=daily_chart1.daily_chart(self.view_daily_chart)
        self.chart2=total_chart1.total_chart(self.view_total_chart)
        world_bar=w_b.world_chart(self.page_world)
        domestic_pie=pie.pie_chart(self.page_local_view_3)
        domestic_bar=bar.bar_chart(self.page_local_view_3)

        #메인
        main_list = domestic_pie.getMain()
        self.init_main(main_list)


    def initSignal(self) :
    #----- push버튼 3종세트
        # 로고/타이틀 클릭시 > 홈화면으로
        self.pushButton_logo.clicked.connect(self.changeMain_0)
        # 국내현황
        self.pushButton_local.clicked.connect(self.changeMain_1)
        self.pushButton_local.clicked.connect(self.changeCategory_0)

        # 국내현황 버튼3개
        self.pushButton_category_local_1.clicked.connect(self.changeLocalView_0)
        self.pushButton_category_local_2.clicked.connect(self.changeLocalView_1)
        self.pushButton_category_local_3.clicked.connect(self.changeLocalView_2)


        # 세계현황
        self.pushButton_world.clicked.connect(self.changeMain_1)
        self.pushButton_world.clicked.connect(self.changeCategory_1)

        # 지도
        self.pushButton_map.clicked.connect(self.changeMain_1)
        self.pushButton_map.clicked.connect(self.changeCategory_2)


    def init_main(self,list):
        self.label_con_1.setText(list[0])
        self.label_con_2.setText(list[1])
        self.label_con_3.setText("<font color=white>"+list[2][4:]+"</font>")
        self.label_con_4.setText("<font color=white>"+list[3]+"</font>")
        self.label_con_5.setText("<font color=white>"+list[4]+"</font>")
        self.label_con_6.setText("<font color=white>"+list[5]+"</font>")
        self.label_con_7.setText("<font color=white>"+list[6][4:]+"</font>")
        self.label_con_8.setText("<font color=white>"+list[7]+"</font>")
        self.label_con_10.setText("<font color=white>"+list[8]+"</font>")
        self.label_con_9.setText("<font color=white>"+list[9]+"</font>")


    # 홈/메인 전환
    def changeMain_0(self): # 홈
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(True)

    def changeMain_1(self): # 메인
        self.stackedWidget.setCurrentIndex(1)





    # 메인 >  전환
    def changeCategory_0(self): # 국내
        self.main_category.setCurrentIndex(0)
        self.pushButton_local.setEnabled(False)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(True)

    def changeCategory_1(self): # 세계
        self.main_category.setCurrentIndex(1)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(False)
        self.pushButton_map.setEnabled(True)

    def changeCategory_2(self): # 지도
        self.main_category.setCurrentIndex(2)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(False)



    # 국내 버튼 누르고 > 하단 뷰창
    def changeLocalView_0(self):
        self.stackedWidget_local_view.setCurrentIndex(0)
    def changeLocalView_1(self):
        self.stackedWidget_local_view.setCurrentIndex(1)
    def changeLocalView_2(self):
        self.stackedWidget_local_view.setCurrentIndex(2)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
