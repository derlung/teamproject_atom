import worldpage
import world_bar
from PyQt5.QtWidgets import *
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
from PyQt5 import QtCore, QtGui, QtWidgets
from world_list import *

class page_world(QWidget,worldpage.Ui_Form):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setupUi(self)
        self.w = world_bar.world_chart(self)
        self.w.setGeometry(QtCore.QRect(0, 0,700,420))
        self.searchButton.clicked.connect(self.click)

    def click(self) :
        item=self.nationInput.text()
        if item in nation:
            ix=nation.index(item)
            value=nation_value[ix]
            self.nation.setText(item)
            self.definite.setText(value)
        else:
            self.nationInput.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = page_world()
    window.show()
    app.exec_()
