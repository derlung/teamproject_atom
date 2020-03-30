from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
import numpy as np
import matplotlib.pyplot as plt
from statistics import *
from matplotlib import font_manager, rc

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

labels = ['남성', '여성']
sizes = [float(gender_m[:-1]),float(gender_w[:-1])]
colors = ['red','blue']
explode = (0.01,0.01)
plt.title("성별 대비")
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()
