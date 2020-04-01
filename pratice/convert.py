from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://www.0404.go.kr/dev/country.mofa?idx=&hash=&chkvalue=no2&stext=&group_idx=&alert_level=0"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

# 확진환자(누적)
world_list=soup.select("#content > div.c_inner > div > div.country_box > div > ul > li")
country=[]
status=[]
english_name=[]
for i in world_list:
    num=i.select_one("a")["href"][19:-3]
    url="http://www.0404.go.kr/dev/country_view.mofa?idx="+num+"&hash=&chkvalue=no2&stext=&group_idx=&alert_level=0"
    res=req.urlopen(url).read()
    soup=BeautifulSoup(res, "html.parser")
    english_name.append(soup.select_one("#content > div.c_inner > div.country_info > h4").string)
    print("파싱 완료")
f = open("나라이름.txt", 'w')
for i in english_name:
    f.write(i+"\n")
f.close()
