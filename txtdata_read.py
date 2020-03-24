import os
import sys,io

sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")

#txt 파일 상대경로 -> 절대경로
path=os.path.join(os.path.dirname(__file__), 'resource/국내확진자_추이.txt')

#txt 파일 열기(읽기 모드)
f = open(path,'r')
lines = f.readlines()

# N: 개수 S:시작날짜 인덱스
N=5
S=5

#데이터 초기화
daily_definite =[]
daily_treate =[]
daily_death =[]

days=[]

total_definite =[]
total_treate=[]
total_death =[]

#가져올 날짜에 해당하는 데이터 가져오기
for i in range(S,S-N,-1):
    line = lines[-i].splitlines()[0].split("\t")
    days.append(line[0])

    del(line[0])
    line = list(map(int,line))

    daily_definite.append(line[0])
    daily_treate.append(line[1])
    daily_death.append(line[2])

    total_definite.append(line[3])
    total_treate.append(line[4])
    total_death.append(line[5])



#파일 닫기
f.close()
