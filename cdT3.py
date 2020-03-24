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

y_value = (float(death_ratio_30[:-1]),float(death_ratio_40[:-1]),float(death_ratio_50[:-1]),float(death_ratio_60[:-1]),float(death_ratio_70[:-1]),float(death_ratio_80[:-1]))
x_name=('30대','40대','50대','60대','70대','80대')
n_groups = len(x_name)
index = np.arange(n_groups)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(index, y_value, tick_label=x_name, align='center')

for p in ax.patches :
    left, bottom, width, height = p.get_bbox().bounds
    ax.annotate("{}%".format(height), (left+width/2, height+0.2), ha='center')

plt.xlabel('나이')
plt.ylabel('치사율')
plt.title('나이대별 치사율')
plt.show()
