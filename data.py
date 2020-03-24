from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://ncov.mohw.go.kr/"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

# 확진환자(누적)
total=soup.select_one("body > div > div.mainlive_container > div > div > div > div.live_left > div.liveNum > ul > li:nth-child(1) > span.num").text

print(total)
# print(soup.find("li", param).string)

# print(total)
