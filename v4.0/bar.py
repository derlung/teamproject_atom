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

class bar_chart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.setupUI()

    def setupUI(self):
        self.setGeometry(-50,270,800,400)

        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        ax=self.fig.add_subplot(111)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)
        self.setLayout(leftLayout)

        ratio = (float(death_ratio_30[:-1]), float(death_ratio_40[:-1]), float(death_ratio_50[:-1]), float(death_ratio_60[:-1]), float(death_ratio_70[:-1]), float(death_ratio_80[:-1]))
        age=['30대','40대','50대','60대','70대','80대']
        index = np.arange(len(age))

        ax.bar(index, ratio, tick_label=age, align='center')

        for p in ax.patches :
            left, bottom, width, height = p.get_bbox().bounds
            ax.annotate("{}%".format(height), (left+width/2, height+0.1), ha='center')

        ax.grid(color='lightgray')
        ax.set_xlabel('나이')
        ax.set_title('나이대별 치사율')
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = bar_chart()
    window.show()
    app.exec_()
