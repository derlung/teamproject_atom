
import sys
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

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

#QWidget.layout 안에 방금 만든 QVBoxLayout()를 넣는다는 느낌
        self.layout = layout
        self.doGraph1()

#그래프1
    def doGraph1(self):
        x = np.arange(0, 10, 0.5)
        y1 = np.sin(x)
        y2 = np.cos(x)

        self.fig.clear()

        ax = self.fig.add_subplot(111)
        ax.plot(x, y1, label="sin(x)")
        ax.plot(x, y2, label="cos(x)", linestyle="--")

        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("sin & cos")
        ax.legend()

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
