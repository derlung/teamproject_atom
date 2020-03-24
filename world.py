from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="https://m.search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98+19+%EC%84%B8%EA%B3%84#"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

# world_total=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div.overseas_summary > strong > em").text
# world_death=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div.overseas_summary > strong > span:nth-child(2)").text
print(soup.select("#_cs_common_production > div > div:nth-child(8) option"))
# china=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div:nth-child(4) > div._flick_root > div > div:nth-child(1) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span")
# china=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div:nth-child(4) > div._flick_root > div > div:nth-child(1) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").string
# italy=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div:nth-child(4) > div._flick_root > div > div:nth-child(1) > div > div > table > tbody > tr:nth-child(2) > td:nth-child(2) > span").text

# print(world_total)
# print(world_death)
# print(china)
# print(italy)
