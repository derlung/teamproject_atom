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

#웹 크롤링
world_total=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div.overseas_summary > strong > em").text
world_death=soup.select_one("#_cs_common_production > div > div:nth-child(8) > div > div.overseas_summary > strong > span:nth-child(2)").text

first_page_nation=soup.select("#_cs_common_production > div.api_subject_bx._svp_list > div:nth-child(8) > div.patients_info > div:nth-child(4) div._flick_root .eg-flick-panel > div.csm_table_area > div.type_basic > table.table > tbody > tr > td:nth-child(1) > span")
first_page_positive=soup.select("#_cs_common_production > div.api_subject_bx._svp_list > div:nth-child(8) > div.patients_info > div:nth-child(4) div._flick_root .eg-flick-panel > div.csm_table_area > div.type_basic > table.table > tbody > tr > td:nth-child(2) > span")

# second_page_nation=soup.select("#_cs_common_production > div.api_subject_bx._svp_list > div:nth-child(8) > div.patients_info > div:nth-child(4) > div._flick_root .eg-flick-panel:nth-child(2) > div.csm_table_area > div.type_basic > table.table > tbody > tr > td:nth-child(1) > span")
# second_page_posivite=soup.select("#_cs_common_production > div.api_subject_bx._svp_list > div:nth-child(8) > div.patients_info > div:nth-child(4) div._flick_root .eg-flick-panel:nth-child(2) > div.csm_table_area > div.type_basic > table.table > tbody > tr > td:nth-child(2) > span")

#리스트
first_nation_list=[]
first_positive_list=[]
# second_nation_list=[]
# second_positive_list=[]

#첫 번째 페이지 나라별 리스트
for a in first_page_nation :
    first_nation_list.append(a.string)
print(first_nation_list)

#첫 번째 페이지 나라의 확진자 리스트
for b in first_page_positive :
    b=b.string.replace(",","")
    first_positive_list.append(int(b))
print(first_positive_list)

#두 번째 페이지 나라별 리스트
# for c in second_page_nation :
#     second_nation_list.append(c.string)
# print(second_nation_list)

#두 번째 페이지 나라의 확진자 리스트
# for d in second_page_posivite :
#     d=d.string.replace(",","")
#     second_positive_list.append(int(d))
# print(second_positive_list)

#전세계 확진자
print('전세계 확진자 : '+world_total)

#전세계 사망자
print('전세계 사망자 : '+world_death)
