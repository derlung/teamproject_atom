from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from statistics import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

class MainDialog(QDialog):
    def __init__(self):

        QDialog.__init__(self,None)
        y_value = [death_ratio_40,death_ratio_50,death_ratio_60,death_ratio_70,death_ratio_80]
        x_name=('40대','50대','60대','70대','80대')
        n_groups = len(x_name)
        index = np.arange(n_groups)

        #그래프 창 가져오기
        fig = plt.Figure()
        ax = fig.add_subplot(111)

        #y축 라벨, 타이틀 이름
        plt.xlabel('age')
        plt.ylabel('death_ratio')
        plt.title('ratio')

        ax.bar(index, y_value, tick_label=x_name,width=0.5)

        canvas = FigureCanvas(fig)
        canvas.draw()

        lay = QHBoxLayout()
        self.setLayout(lay)
        lay.addWidget(canvas)
        canvas.show()


app = QApplication(sys.argv)
main = MainDialog()
main.show()
app.exec_()
