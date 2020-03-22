import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

#엑셀 파일 위치 (수정)
data = pd.read_excel('resource/대한민국_코로나_추이.xlsx',convert_float = True)

daily_definite = data["일일_확진자"].tail(5)
daily_treate = data["일일_완치자"].tail(5)
daily_death = data["일일_사망자"].tail(5)

days = data["날짜"].tail(5)

total_definite = data["누적_확진자"].tail(5)
total_treate = data["누적_완치자"].tail(5)
total_death = data["누적_사망자"].tail(5)
