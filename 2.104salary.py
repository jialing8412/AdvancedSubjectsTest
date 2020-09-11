# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:12:20 2019

@author: jialing
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url=('https://www.104.com.tw/jb/career/department/navigation?browser=1&degree=3')

r=requests.get(url, headers=headers)
r.encoding = 'utf-8'

count = 0
soup = BeautifulSoup(r.text,"lxml")

i=0
school_list=[]
school_list2=[]

for link in soup.find_all('a'):
    link_a = link.get('href')
    school_link='https://www.104.com.tw'+str(link_a) 
    school_name=link.get_text()
    if(i>0):
        school_list.append(school_name)
        school_list2.append(school_link)
    i+=1
school_data_df=pd.DataFrame({"school_name":school_list,"school_link":school_list2})

pd.set_option('display.width', 100000)
pd.set_option('display.max_rows', None)
major_data_df_all=pd.DataFrame()
l=0
for n in school_data_df.school_link:
    r1=requests.get(n, headers=headers)
    r1.encoding = 'utf-8'
    soup = BeautifulSoup(r1.text,"lxml")
    j=0
    major_name_list=[]
    major_link_list=[]
    school_list_name=[]
    for li in soup.find_all('a'):
        link_b = li.get('href')
        major_link='https://www.104.com.tw'+str(link_b)
        major_name=li.get_text()

        if(j>2):
            school_list_name.append(school_data_df.school_name[l])
            major_name_list.append(major_name)
            major_link_list.append(major_link)
        j+=1
    major_data_df=pd.DataFrame({"school_name":school_list_name,"major_name":major_name_list,"major_link":major_link_list})
    l+=1
    major_data_df_all=major_data_df_all.append(major_data_df,ignore_index=True)



import time
import csv
pd.set_option('display.max_column', None)
salary_list=[]
salary_data_df_all=pd.DataFrame()
for s in major_data_df_all.major_link:
    r2=requests.get(s, headers=headers)
    r2.encoding = 'utf-8'
    time.sleep(4)
    r2text=r2.text
    count = 0
    soup = BeautifulSoup(r2.text,"lxml")
    sle_number=soup.find_all("div",class_="arrow-box-right cf hide")
    count=len(sle_number)
    data_list=[]
    for x in sle_number:
        percent_data=x.findAll("strong")
        for y in percent_data:
            data_number=y.get_text()
            data_list.append(data_number)

    if(data_list==[]):
        data_list.append(-1)
        salary=0
    else:
        sum_ = float(data_list[0]) * float(data_list[1])
        for i in range(0,6):
            sum_+=(float(data_list[(i+1)*2])-float(data_list[2*i]))* float(data_list[2*i+3])

        salary=int(sum_/100)
    salary_list.append(salary)
    data_df=pd.DataFrame([data_list])

salary_data_df_all=pd.DataFrame({"school_name":major_data_df_all.school_name,"major_name":major_data_df_all.major_name,"major_link":major_data_df_all.major_link,"salary":salary_list})

salary_data_df_all.to_csv('OutputSalary.csv',encoding='utf-8-sig')

print("跑完了~~~~")
