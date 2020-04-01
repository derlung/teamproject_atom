from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

hi=soup.select("#content > div > div:nth-child(5) > div.inner > div > table > tbody > tr")
# print(hi)

nation_value=[]
nation=[]
nation_value_dict=[]
for i,v in enumerate (hi) :
    if i==len(hi)-1 :
        world_definite_total = str(v.select_one("td").text.replace("\t","").splitlines())
    else:
        country=v.select_one(".w_bold").string
        num=v.select_one("td:nth-of-type(2)").text.replace("\t","").splitlines()
    nation_value.append(num[0])
    nation_value_dict.append(int(num[0][:-1].replace(",","")))
    nation.append(country)

#세계 확진자
# print(nation_value)
#
# #나라 이름
# print(nation)



    def setTableWidgetData(self,dict_data):
        self.tableWidget.setHorizontalHeaderLabels(["나라","확진자 수")
        self.tableWidget.setRowCount(len(dict_data))
        self.tableWidget.setColumnCount(2)
        i=0
        for (key,elem) in enumerate(many.items()) :
            j=0
            self.tableWidget.setItem(i,j,QTableWidgetItem(key))
            j+=1
            self.tableWidget.setItem(i,j,QTableWidgetItem(elem))
            i+=1

def get_many(self):
    return many

# Create a zip object from two lists
zipbObj = zip(nation, nation_value_dict)

# Create a dictionary from zip object
dictOfWords = dict(zipbObj)
print(dictOfWords)
res = sorted(dictOfWords.items(),key=lambda x:x[1])
print("적은 순  ",res)
res = sorted(dictOfWords.items(),key=lambda x:x[1],reverse=True)
print("많은 순  ",res)
