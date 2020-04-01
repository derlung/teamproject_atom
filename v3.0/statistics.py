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
total=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(1) > span.num").text
definite=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(2) > span.num").text
treat=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(3) > span.num").text
death=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(4) > span.num").text

check=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.info_core > ul > li:nth-child(1) > span.num").text
check_finish=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.info_core > ul > li:nth-child(2) > span.num").text
definite_total=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.info_core > ul > li:nth-child(3) > span.num").text


treatment=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.chart_d > div > div.cc_figure > p.numinfo1 > span.num_rnum").text
positive=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.chart_d > div > div.cc_figure > p.numinfo2 > span.num_rnum").text
negative=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveToggleOuter > div > div.live_left > div.liveTest.main_box_toggle > div.chart_d > div > div.cc_figure > p.numinfo3 > span.num_rnum").text

yesterday=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
yesterday_recovery=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
yesterday_treatment=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
yesterday_death=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text


today_definite = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text[8:-1]
today_death = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text[3:-1]
today_treat = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text[3:-1]

plus_total = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(1) > span.before").text
plus_definite=soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(2) > span.before").text
plus_death =soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(3) > span.before").text
plus_treat =soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div > ul > li:nth-child(4) > span.before").text
url="http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")

gender_m=soup.select_one("#content > div > div:nth-child(16) > table > tbody > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)").text
gender_w=soup.select_one("#content > div > div:nth-child(16) > table > tbody > tr:nth-child(2) > td:nth-child(3) > span:nth-child(1)").text



death_ratio_30=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(6) > td:nth-child(4) > span").string
death_ratio_40=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(5) > td:nth-child(4) > span").string
death_ratio_50=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(4) > td:nth-child(4) > span").string
death_ratio_60=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(3) > td:nth-child(4) > span").string
death_ratio_70=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(2) > td:nth-child(4) > span").string
death_ratio_80=soup.select_one("#content > div > div:nth-child(19) > table > tbody > tr:nth-child(1) > td:nth-child(4) > span").string



# print('확진환자 : '+total)
# print('완치환자 : '+definite)
# print('치료 중 환자 : '+treat)
# print('사망 : '+death)
# print('누적 검사 수 : '+check)
# print('누적 검사 완료 수 : '+check_finish)
# print('누적 확진률 : '+definite_total)
# print('검사 중 : '+treatment)
# print('결과 양성 : '+positive)
# print('결과 음성 : '+negative)
# print('남성비 : '+gender_m)
# print('여성비 : '+gender_w)
# print('30대 치사율 : '+death_ratio_30)
# print('40대 치사율 : '+death_ratio_40)
# print('50대 치사율 : '+death_ratio_50)
# print('60대 치사율 : '+death_ratio_60)
# print('70대 치사율 : '+death_ratio_70)
# print('80대 치사율 : '+death_ratio_80)
# print('전일 대비 확진환자 : '+yesterday)
# print('전일 대비 완치환자 : '+yesterday_treatment)
# print('전일 대비 사망 : '+yesterday_death)
print("일일 확진자:"+today_definite)
print("일일 완치자:"+today_treat)
