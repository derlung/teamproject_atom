import urllib.request as req
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

f = open("나라이름.txt", 'r')

list =f.readlines()
english=[]
korean=[]
for j,i in enumerate(list):
    if(j==len(list)-1):
        korean.append(i.split("(")[0])
        english.append(i.split("(")[2][:-2])
    elif i=="마카오(중국)(Macau)\n":
        korean.append(i.split("(")[0])
        english.append(i.split("(")[2][:-2])
    else:
        korean.append(i.split("(")[0])
        english.append(i.split("(")[1][:-2])

# print(english)
# print(korean)
f.close()
