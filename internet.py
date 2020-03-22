
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

#콤보박스 (그래프 선택)
        cb = QComboBox()
        cb.addItem('Graph1')
        cb.addItem('Graph2')

#콤보에서 선택 이벤트는 activated 전달값 타입은 [str]식으로 전달한다
        cb.activated[str].connect(self.onComboBoxChanged)
        layout.addWidget(cb)

#QWidget.layout 안에 방금 만든 QVBoxLayout()를 넣는다는 느낌
        self.layout = layout

#currentText (콤보박스 초기화 값으로 그래프 초기화)
        self.onComboBoxChanged(cb.currentText())

    def onComboBoxChanged(self, text):
        if text == 'Graph1':
            self.doGraph1()
        elif text == 'Graph2':
            self.doGraph2()

#그래프1  현재 ComboBox에서 선택된 항목의 글자를 반환합니다.
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

#그래프2
    def doGraph2(self):
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = X**2 + Y**2

        self.fig.clear()

        ax = self.fig.gca(projection='3d')
        ax.plot_wireframe(X, Y, Z, color='black')

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
