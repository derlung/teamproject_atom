import os
import sys,io
from datetime import datetime
from statistics import *

class txtdata:
    def __init__(self):
        #데이터변수
        self.lines=[]
        self.daily_definite =[]
        self.daily_treate =[]
        self.daily_death =[]

        self.total_days=[]
        self.daily_days=[]

        self.total_definite =[]
        self.total_treate=[]
        self.total_death =[]
        self.lines=[]

        #최대값변수
        self.max_ddef=0
        self.max_dtre=0
        self.max_ddeth=0

        self.max_tdef=0
        self.max_ttre=0
        self.max_tdeth=0

        #한글 깨짐 방지
        sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")


        #txt 데이터 가져오기
        self.read()
        #데이터 업데이트
        self.update()
        #최댓값 변수 설정
        self.getMax()

    #데이터 업데이트
    def update(self):
        now = datetime.now()
        lastdate = self.lines[len(self.lines)-1][:6]
        today = str(now.month)+"월 "+str(now.day)+"일"
        l = lastdate.strip()
        last = datetime.strptime(l,"%m월 %d일")
        toda = datetime.strptime(today,"%m월 %d일")
        if toda<=last :
            return
        else:
            #txt 파일 상대경로 -> 절대경로
            path=os.path.join(os.path.dirname(__file__), '../resource/국내확진자_추이.txt')
            #txt 파일 열기(읽기 모드)
            lastdata=self.lines[len(self.lines)-1].replace("\n","").split("\t")
            f = open(path,'a')
            today_data = today+"\t"+today_definite+"\t"+today_treat+"\t"+plus_death[2:-1]+"\t"
            today_data += str(int(lastdata[4])+int(today_definite))+"\t"+str(int(lastdata[5])+int(today_treat))+"\t"+str(int(lastdata[6])+int(today_death))+"\n"
            f.write(today_data)
            f.close()



    #txt데이터 가져오기
    def read(self):
        #txt 파일 상대경로 -> 절대경로
        path=os.path.join(os.path.dirname(__file__), '../resource/국내확진자_추이.txt')

        #txt 파일 열기(읽기 모드)
        f = open(path,'r')
        self.lines = f.readlines()

        #파일 닫기
        f.close()

    #가져올 날짜에 해당하는 데이터 가져오기
    # N: 개수 S:끝날짜 인덱스
    def getDaily(self,S,N):
        self.daily_days=[]
        self.daily_definite=[]
        self.daily_treate=[]
        self.daily_death=[]
        for i in range(S-N,S,1):
            line = self.lines[i].splitlines()[0].split("\t")
            self.daily_days.append(line[0])

            del(line[0])
            line = list(map(int,line))

            self.daily_definite.append(line[0])
            self.daily_treate.append(line[1])
            self.daily_death.append(line[2])

    #가져올 날짜에 해당하는 데이터 가져오기
    # N: 개수 S:끝날짜 인덱스
    def getTotal(self,S,N):
        self.total_days=[]
        self.total_definite=[]
        self.total_treate=[]
        self.total_death=[]
        for i in range(S-N,S,1):
            line = self.lines[i].splitlines()[0].split("\t")
            self.total_days.append(line[0])
            del(line[0])
            line = list(map(int,line))
            self.total_definite.append(line[3])
            self.total_treate.append(line[4])
            self.total_death.append(line[5])

    #총 데이터 개수 -> 스크롤바 이용
    def getNum(self):
        return len(self.lines)

    #가져온 날짜값 이용해서 한줄 데이터 가져오기
    def getDetail(self,selDate):
        for i in self.lines:
            day =  i.splitlines()[0].split("\t")[0]
            if selDate==day:
                return i.splitlines()[0].split("\t")

    #그래프이용하기위해 값 가장 높은 거 가져오기
    def getMax(self):
        definite_d=[]
        treate_d = []
        death_d=[]
        definite_t=[]
        treate_t = []
        death_t=[]
        for i in self.lines:
            line = i.splitlines()[0].split("\t")
            definite_d.append(int(line[1]))
            treate_d.append(int(line[2]))
            death_d.append(int(line[3]))
            definite_t.append(int(line[4]))
            treate_t.append(int(line[5]))
            death_t.append(int(line[6]))
        self.max_ddef=max(definite_d)
        self.max_dtre=max(treate_d)
        self.max_ddeth=max(death_d)
        self.max_tdef=max(definite_t)
        self.max_ttre=max(treate_t)
        self.max_tdeth=max(death_t)

if __name__=="__main__":
    window = txtdata()
