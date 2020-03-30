from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from world import *
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

class world_chart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 100, 800, 500)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        ax = self.fig.add_subplot(111)
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)
        self.setLayout(leftLayout)

        nations = first_nation_list
        nations.reverse()
        index = np.arange(len(nations))
        patients = first_positive_list
        patients.reverse()

        for i,v in enumerate(nations) :
            str_val="%d명" % patients[i]
            ax.text(patients[i],v,str_val, fontsize=10, horizontalalignment='left', verticalalignment='center')

        ax.barh(nations, patients, align='center', alpha=0.5)
        ax.set_xlabel('전세계 확진자 수')
        ax.set_title('전세계 코로나 현황')
        ax.grid(color='lightgray')

        self.canvas.draw()
