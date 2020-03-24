
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from txtdata_read import *
import mplcursors

#그래프 양쪽 범례 사용

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


#UI 크기
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 800, 600)


#UI초기화
    def initUI(self):
#figure 그래프 창 설정 -> canvas 그래프 표시 창
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)


#vertical BoxLayout () - 수평
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)


#버튼 (그래프 선택)
        self.dailyButton = QPushButton("일일 통계")
        self.totalButton = QPushButton("누적 통계")


#콤보에서 선택 이벤트는 activated 전달값 타입은 [str]식으로 전달한다
        self.dailyButton.clicked.connect(lambda:self.onButtonClick("일일 통계"))
        self.totalButton.clicked.connect(lambda:self.onButtonClick("누적 통계"))
        self.onButtonClick("일일 통계")

        layout.addWidget(self.dailyButton)
        layout.addWidget(self.totalButton)

#QWidget.layout 안에 방금 만든 QVBoxLayout()를 넣는다는 느낌
        self.layout = layout

#currentText (콤보박스 초기화 값으로 그래프 초기화)
        # self.onComboBoxChanged(cb.currentText())

    def onButtonClick(self, text):
        if text == "일일 통계":
            self.dailyGraph()
        elif text == "누적 통계":
            self.totalGraph()

#그래프1  현재 ComboBox에서 선택된 항목의 글자를 반환합니다.
    def dailyGraph(self):
        bars=["확진자","완치자","사망자"]
        values = [daily_definite , #확진자
                  daily_treate,                 #완치자
                  daily_death  ]               #사망자
        ind = np.arange(N)
        width = 0.35

        self.fig.clear()

        ax = self.fig.add_subplot(111)
        #y축 라벨, 타이틀 이름
        ax.set_ylabel('인원(단위 : 명)')
        ax.set_title('일일 코로나 추이')

        #그래프 바x축 위치 정하기 및 그래프 창에 붙이기
        indx = self.compute_pos(N,width,0,bars)
        grap_def=ax.bar(indx,values[0],width,label=bars[0])

        indx = self.compute_pos(N,width,1,bars)
        grap_treat=ax.bar(indx,values[1],width,label=bars[1])

        #오른쪽 범례 그래프 만들기
        ax2 = ax.twinx()
        ax.set_xticklabels(days)
        ax.set_xticks(ind+width/20) #X축 라벨의 글자가 하나씩 밀려서 사용
        grap_death=ax2.plot(ind,values[2],color="blue",label=bars[2])


        for p in ax.patches:
            left, bottom, width, height = p.get_bbox().bounds
            ax.annotate("%d"%(height), (left+width/2, height*1.01), ha='center')

        # Solution for having two legends
        cursor1 = mplcursors.cursor([grap_def,grap_treat],hover=True)
        # cursor1.connect("add", lambda sel: sel.annotation.set_text(days[sel.target.index]))
        cursor1.connect("add",lambda sel:sel.annotation.set_text(days[sel.target.index]))
        cursor2=mplcursors.cursor([grap_def,grap_treat])
        cursor2.connect("add",self.click_cursor)
        self.canvas.draw()


    def click_cursor(self,sel):
        print(days[sel.target.index])
        sel.annotation.set_bbox(None)
        sel.annotation.set_text(None)
#그래프2
    def totalGraph(self):
        self.setGeometry(200, 200, 1000, 600)
        bars=["확진자","완치자","사망자"]
        values = [total_definite , #확진자
                  total_treate,                 #완치자
                  total_death  ]               #사망자
        ind = np.arange(N)
        width = 0.35

        self.fig.clear()

        ax = self.fig.add_subplot(111)
        #y축 라벨, 타이틀 이름
        ax.set_ylabel('인원(단위 : 명)')
        ax.set_title('누적 코로나 추이')

        #그래프 바x축 위치 정하기 및 그래프 창에 붙이기
        for i in range(len(values)-1):
            indx = self.compute_pos(N,width,0,bars)
            ax.bar(indx,values[i],width,label=bars[i])


        ax.set_xticklabels(days)
        ax.set_xticks(ind+width/20) #X축 라벨의 글자가 하나씩 밀려서 사용
        ax.plot(ind,values[2],color="blue",label=bars[2])


        ax.legend()

        self.canvas.draw()

#xticks = x축개수, width = bar넓이 , i번째바 , ind = 바개수
    def compute_pos(self,xticks, width, i, bars):
        ind = np.arange(xticks)
        n = len(bars)-1
        correction = i-0.5*(n-1)
        return ind + width*correction
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
