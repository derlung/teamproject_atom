import sys,io
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        N = 5
        models=["confirm","death","cure"]
        values = [[100,200,150,50,70], #확진자
                  [2,1,5,7,3],                 #사망자
                  [70,80,50,60,50]]                  #완치자
        ind = np.arange(N)
        width = 0.35


        #그래프 창 가져오기
        fig = plt.Figure()
        ax = fig.add_subplot(111)


        #y축 라벨, 타이틀 이름
        plt.ylabel('명')
        plt.title('일일 코로나 추이')


        #그래프 바x축 위치 정하기 및 그래프 창에 붙이기
        for i in range(len(values)-1):
            indx = self.compute_pos(5,0.35,i,models)
            ax.bar(indx,values[i],width)


        ax.set_xticklabels(['G1','G2','G3','G4','G5'])
        ax.set_xticks(ind+width/20) #X축 라벨의 글자가 하나씩 밀려서 사용
        ax.plot(ind,values[2],color="blue")
        # ax.bar(y2,(20,30,40,50,60),color="red",width=0.35)
        canvas = FigureCanvas(fig)
        canvas.draw()


        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(canvas)
        canvas.show()


#xticks = x축개수, width = bar넓이 , i번째바 , ind = 바개수
    def compute_pos(self,xticks, width, i, models):
        ind = np.arange(xticks)
        n = len(models)-1
        correction = i-0.5*(n-1)
        return ind + width*correction


app = QApplication(sys.argv)
main = MainDialog()
main.show()
app.exec_()
