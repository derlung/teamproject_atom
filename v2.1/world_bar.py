from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from world import *
from matplotlib import font_manager, rc
from matplotlib import style

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

nations = first_nation_list
nations.reverse()
index = np.arange(len(nations))
patients = first_positive_list
patients.reverse()
plt.rcParams["figure.figsize"]=(15,8) #차트 사이즈

for i,v in enumerate(nations) :
    str_val="%d명" % patients[i]
    plt.text(patients[i],v,str_val, fontsize=10, horizontalalignment='left', verticalalignment='center')

plt.barh(nations, patients,align='center', alpha=0.5)
plt.yticks(index, nations)
plt.xlabel('전세계 확진자 수')
plt.title('전세계 코로나 현황')
plt.grid(color='lightgray')

plt.show()
