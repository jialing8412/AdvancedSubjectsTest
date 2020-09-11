# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:01:03 2020

@author: jialing
"""
#judgment 判斷 是分組或是
import pandas as pd
import csv


input_file='OutputStatus.csv'
data=[]
did=[]
school=[]
name109=[]
name108=[]
change=[]


with open(input_file, newline='',encoding="utf-8") as csvfile:
  rows = csv.reader(csvfile)
  for row in rows:
    data.append(row)

for x in range(len(data)):
    if x==len(data)-1:
        pass
    elif x==0:
        pass
    else:
        if '--' in data[x+1]:
            if '--' in data[x+1][2]:
                did.append(data[x][0])
                if data[x][1]=='--':
                    pass
                else:
                    school_name=data[x][1] #為了可以填下一個
                school.append(school_name)
                if data[x][2]=='--':
                    pass
                else:
                    name_109=data[x][2] #為了可以填下一個
                name109.append(name_109)
                name108.append(data[x][3])
                status='合併'
                change.append(status)
            elif '--' in data[x+1][3]:
                did.append(data[x][0])
                school.append(data[x][1])
                name109.append(data[x][2])
                if data[x][3]=='--':
                    pass
                else:
                    name_108=data[x][3] #為了可以填下一個
                name108.append(name_108)
                status='分組'
                change.append(status)
        elif '--' in data[x][2]:
                did.append(data[x][0])
                school.append(school_name)
                name109.append(name_109)
                name108.append(data[x][3])
                status='合併'
                change.append(status)
        elif '--' in data[x][3]:
                did.append(data[x][0])
                school.append(data[x][1])
                name109.append(data[x][2])
                name108.append(name_108)
                status='分組'
                change.append(status)
        else:
            did.append(data[x][0])
            school.append(data[x][1])
            name109.append(data[x][2])
            name108.append(data[x][3])
            status='更名'
            change.append(status)
df=pd.DataFrame({"校碼":did,"校名":school,"109招生系組名稱":name109,"108學年度原系組名稱":name108,"狀態":change})
df.to_csv("OutputStatus2.csv", encoding="utf_8_sig",index=False)