import sys,io
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5 import uic,QtCore
from chart_ui1 import Ui_MainWindow
from daily_chart import MyWindow as dcht #일일 차트 UI
from total_chart import MyWindow as tcht #누적 차트 UI


# form_class = uic.loadUiType('D:/atom_python/section6/lib/YouView.ui')[0]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")


class Main(QMainWindow,Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자 함수 호출
        self.setupUi(self) #함수선언

        #시그널 초기화작업
        self.initSignal()
        self.dchart=dcht(self.page)
        self.dchart.setGeometry(QtCore.QRect(40, 50, 421, 321))
        self.tchart=tcht(self.page_2)
        self.tchart.setGeometry(QtCore.QRect(40, 50, 421, 321))

    #기본 UI 비활성화
    def initAuthLock(self):
        # self.previewButton.setEnabled(False)
        pass


    #시그널 초기화
    def initSignal(self):
        self.pushButton.clicked.connect(self.pagechange1)
        self.pushButton_2.clicked.connect(self.pagechange2)

    def pagechange1(self):
        self.stackedWidget.setCurrentIndex(0)

    def pagechange2(self):
        self.stackedWidget.setCurrentIndex(1)


    # @pyqtSlot()#명시적 표현
    # def authCheck(self):
    #     adg = AuthDialog()
    #     adg.exec_()
    #     self.user_id = adg.user_id
    #     self.user_pw = adg.user_pw

        #이 부분에서 필요한 경우 실제 로컬 DB 또는 서버 연동 후
        #유저 정보 및 사용자 유효기간을 체크하는 코딩


if __name__=="__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()
