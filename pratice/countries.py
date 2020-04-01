from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://www.0404.go.kr/dev/country.mofa?idx=&hash=&chkvalue=no2&stext=&group_idx=&alert_level=0"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

# 확진환자(누적)
world_list=soup.select("#content > div.c_inner > div > div.country_box > div > ul > li")
country=[]
status=[0]*len(world_list)

for i,v in enumerate(world_list):
    country.append(v.select_one("a").text)
    s=v.select("strong")

    for d in s:
        b=d.select_one("img")["alt"]
        if(b=="특별여행주의보" or b=="여행금지"):
            status[i]=1
        else:
            status[i]=0
df=pd.DataFrame({'name':country,'ban':status})
df.to_csv('country_ban.csv')
