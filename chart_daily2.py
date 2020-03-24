import sys,io
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from xsldata_read import *
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        N = 5
        bars=["확진자","완치자","사망자"]
        values = [daily_definite , #확진자
                  daily_treate,                 #완치자
                  daily_death    ]              #사망자33
        ind = np.arange(N)
        width = 0.35

        #그래프 창 가져오기
        fig = plt.Figure()
        ax = fig.add_subplot(111)

        #y축 라벨, 타이틀 이름
        plt.ylabel('인원(단위 : 명)')
        plt.title('일일 코로나 추이')

        #그래프 바x축 위치 정하기 및 그래프 창에 붙이기
        for i in range(len(values)-1):
            indx = self.compute_pos(5,0.35,i,bars)
            ax.bar(indx,values[i],width,label=bars[i])


        ax.set_xticklabels(days)
        ax.set_xticks(ind+width/20) #X축 라벨의 글자가 하나씩 밀려서 사용
        ax.plot(ind,values[2],color="blue",label=bar[2])

        canvas = FigureCanvas(fig)
        canvas.draw()

        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(canvas)
        canvas.show()

#xticks = x축개수, width = bar넓이 , i번째바 , ind = 바개수
    def compute_pos(self,xticks, width, i, bars):
        ind = np.arange(xticks)
        n = len(bars)-1
        correction = i-0.5*(n-1)
        return ind + width*correction

app = QApplication(sys.argv)
main = MainDialog()
main.show()
app.exec_()
