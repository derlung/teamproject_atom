from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://ncov.mohw.go.kr"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")
korea = soup.select("#main_maplayout>button")
local_data = []
for i,v in enumerate(korea):
    if(i==len(korea)-1):
        break
    local_data.append(i.select_one("span.name").string)
    lo
