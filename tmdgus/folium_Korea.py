
# Import libraries
import pandas as pd
import folium

#시간 처리 관련
import time
# bs4
from bs4 import BeautifulSoup
#selenium 관련 임포트
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from seoul import *

import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



state_geo = 'D://pro/Folium_Test/TL_SCCO_SIG_WGS84.json'



state_data = cars

# Initialize the map:
m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
print(state_data)
# Add the color for the chloropleth:

m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

folium.LayerControl().add_to(m)

# Save to html
m.save('folium_kr.html')
#크롬
chrome_option=Options()

browser=webdriver.Chrome("D:/atom_python/section7/webdriver/chrome/chromedriver.exe")
browser.get("D:/pro/Folium_Test/folium_kr.html")
