from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from statistics import *
from matplotlib import font_manager, rc
from matplotlib import style
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

class pie_chart(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUI()

    def setupUI(self):
        self.setGeometry(180, -20, 350, 350)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        ax=self.fig.add_subplot(111)

        labels = ['남성', '여성']
        sizes = [float(gender_m[:-1]),float(gender_w[:-1])]
        colors = ['blue','red']
        explode = (0.01,0.01)
        ax.set_title("성별 대비")
        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)
        self.setLayout(leftLayout)
        self.canvas.draw()

    def getMain(self):
        list = []
        list.append(today_definite)
        list.append(today_treat)
        list.append(total)
        list.append(definite)
        list.append(treat)
        list.append(death)
        list.append(plus_total)
        list.append(plus_definite)
        list.append(plus_treat)
        list.append(plus_death)
        return list

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pie_chart()

    window.show()
    app.exec_()
