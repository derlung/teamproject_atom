from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from statistics import *
from matplotlib import font_manager, rc
from matplotlib import style

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

ratio = (float(death_ratio_30[:-1]),float(death_ratio_40[:-1]),float(death_ratio_50[:-1]),float(death_ratio_60[:-1]),float(death_ratio_70[:-1]),float(death_ratio_80[:-1]))
age=['30대','40대','50대','60대','70대','80대']
index = np.arange(len(age))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(index, ratio, tick_label=age, align='center')

for p in ax.patches :
    left, bottom, width, height = p.get_bbox().bounds
    ax.annotate("{}%".format(height), (left+width/2, height+0.1), ha='center')

plt.rcParams["figure.figsize"]=(10,5) #차트 사이즈
plt.grid(color='lightgray')
plt.xlabel('나이')
plt.title('나이대별 치사율')
plt.show()
