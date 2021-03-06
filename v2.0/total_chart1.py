from chart_ui2 import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib import font_manager, rc
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import txtdata_read
import mplcursors
import random


class total_chart(QWidget,Ui_Form):
    def __init__(self,parent):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
        rc('font', family=font_name)
        self.initUI()
        self.initSignal()


#UI초기화
    def initUI(self):

        #차트 변수
        self.c1=True
        self.c2=True
        self.c3=True

        #차트 생성 및 초기화
        self.m = PlotCanvas(self, width=7, height=5)
        self.m.move(20,30)
        self.m.totalGraph(50,5,self.c1,self.c2,self.c3)

        #콤보박스 모두 체크로 셋팅
        self.cb_definite.setChecked(True)
        self.cb_treate.setChecked(True)
        self.cb_death.setChecked(True)

        #스크롤바
        self.ScrollbarDate.setMinimum(5)
        self.ScrollbarDate.setMaximum(self.m.getdateNum())
        self.ScrollbarDate.setValue(self.ScrollbarDate.maximum())
        self.date=self.ScrollbarDate.maximum()

#시그널 초기화
    def initSignal(self):
        #콤보박스 모두 체크시 변수 변경
        self.cb_definite.stateChanged.connect(self.checkBoxState)
        self.cb_treate.stateChanged.connect(self.checkBoxState)
        self.cb_death.stateChanged.connect(self.checkBoxState)
        self.ScrollbarDate.valueChanged.connect(self.datechange)

#체크박스 변경시 그래프 변경
    def checkBoxState(self):
        self.c1=self.cb_definite.isChecked()
        self.c2=self.cb_treate.isChecked()
        self.c3=self.cb_death.isChecked()
        self.m.totalGraph(self.date,5,self.c1,self.c2,self.c3)

#슬라이더바 변경시 날짜 변경
    def datechange(self):
        self.label.setText(str(self.ScrollbarDate.value()))
        self.date=self.ScrollbarDate.value()
        self.m.totalGraph(self.date,5,self.c1,self.c2,self.c3)


#차트
class PlotCanvas(FigureCanvas):
    txtd = txtdata_read.txtdata()
    def __init__(self, parent=None, width=8, height=6, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.num = self.txtd.getNum()
        # self.totalGraph(self.num,5,True,True,True)


    def totalGraph(self,S,N,c1=True,c2=True,c3=True):
        self.txtd.getTotal(S,N)
        N=5
        bars=["확진자","완치자","사망자"]
        values = [self.txtd.total_definite , #확진자
                  self.txtd.total_treate,    #완치자
                  self.txtd.total_death  ]   #사망자
        ind = np.arange(N)
        width = 0.35

        self.figure.clear()

        ax = self.figure.add_subplot(111)
        #y축 라벨, 타이틀 이름
        ax.set_ylabel('인원(단위 : 명)')
        ax.set_title('누적 코로나 추이')

        grap_def=None
        grap_treat=None
        grap_death=None
        cursor_list = []
        #그래프 개수 (체크박스에 따라)
        bar_num=1
        if(c1==True):
            bar_num+=1
        if(c2==True):
            bar_num+=1

        #확진작 그래프
        if(c1==True):
            indx = self.compute_pos(N,width,0,bar_num)
            grap_def=ax.bar(indx,values[0],width,color='#003c7d',label=bars[0])
            cursor_list.append(grap_def)

        if(c2==True):
            indx = self.compute_pos(N,width,1,bar_num)
            grap_treat=ax.bar(indx,values[1],width,color='#7cc26e',label=bars[1])
            cursor_list.append(grap_treat)

        #x축 라벨 만들기
        ax.set_xticklabels(self.txtd.total_days)
        ax.set_xticks(ind+width/20) #X축 라벨의 글자가 하나씩 밀려서 사용
        # Put a legend to the right of the current axis
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        #오른쪽 범례 그래프 만들기

        if(c3==True):
            ax2 = ax.twinx()
            grap_death=ax2.plot(ind,values[2],color='#121149',label=bars[2])
            ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        for p in ax.patches:
            left, bottom, width, height = p.get_bbox().bounds
            ax.annotate("%d"%(height), (left+width/2, height*1.01), ha='center')


        if len(cursor_list)>0:
            cursor1 = mplcursors.cursor(cursor_list,hover=True)
            cursor1.connect("add",lambda sel:sel.annotation.set_text(self.txtd.total_days[sel.target.index]))
            cursor2=mplcursors.cursor(cursor_list)
            cursor2.connect("add",self.click_cursor)

        self.draw()


    def click_cursor(self,sel):
        sel.annotation.set_bbox(None)
        sel.annotation.set_text(None)


#xticks = x축개수, width = bar넓이 , i번째바 , ind = 바개수
    def compute_pos(self,xticks, width, i, bars):
        ind = np.arange(xticks)
        n = bars-1
        correction = i-0.5*(n-1)
        return ind + width*correction

    def getdateNum(self):
        return self.txtd.getNum()

app = QApplication(sys.argv)
dlg =total_chart()
dlg.show()
app.exec_()
