# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:21:31 2019

@author: jialing
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd




school_link_list=[]
school_name_list=[]
headers = {'Cookie':'__cfduid=db4594c522553734ab9e7bd16ba4361651565180630; cf_clearance=f43765aad8292fb87022e1353c19a399bc0de2bd-1565180635-604800-150',\
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'}
first_url="https://www.com.tw/exam/university_list108.html"

r=requests.get(first_url, headers=headers)#將網頁資料GET下來
print(r)
soup = BeautifulSoup(r.text,"lxml")
print(r.text)

a=[]
for link in soup.findAll('a'):
    link_a = link.get('href')
    a.append(link_a) 
    if ('_108.html') in link_a:
        school_link="https://www.com.tw/exam/"+link_a
        school_name=link.get_text()
        school_name_list.append(school_name)
        school_link_list.append(school_link)
        
school_data_df=pd.DataFrame({"school_name":school_name_list,"school_link":school_link_list})

c=0
did_all=[]
major_all=[]
score_all=[]
score_avg_all=[]
school_all=[]
school_major_all=[]
xc=0

for n in school_data_df.school_link:
    data=[]
    did=[]
    major=[]
    score=[]
    school=[]
    j=[]
    i=0
    #print(n)
    school_count=school_data_df.school_name[c]
    headers2 = {'Cookie':'__cfduid=d04b49c39b53c4071a7e144189b5651281565200938; cf_clearance=6df8efd778a67ee5aaaee9747e10f5dc79006570-1565200942-604800-150',\
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    major_r=requests.get(n, headers=headers2)
    soup = BeautifulSoup(major_r.text,"lxml")
    is_want_data=False#判斷遇到的資料是不是我們要的
    for link in soup.findAll('div'):
        a=link.get_text()
        if a=='校系代碼':#如果遇到校系代碼後，後面的資料是我們要的
            is_want_data=True
        if is_want_data==True:
            a=a.strip("\n")
            if a!="":
                data.append(a)
    count=1  
    
    for x in data:
        if x==' 祝您金榜題名':
            break
        elif x=='校系代碼':
            pass
        elif x=='採計科目':
            pass
        elif x=='系名':
            pass
        elif x=='錄取分數(平均)':
            pass
        elif count%4==1:
            #did
            x=x.strip("(")
            x=x.strip(")")
            did.append(x)
            did_all.append(x)
            count+=1
            xc+=1
        elif count%4==2:
            #科系名
            x=x.split("-")
            de='(男)'
            de2='(女)'
            if (de in x[0]):
                x[0],y=x[0].split(de)
            elif (de2 in x[0]):
                x[0],y=x[0].split(de2)
            major.append(x[0])
            major_all.append(x[0])    
            school_major_all.append(school_count+" "+x[0])
            count+=1
            xc+=1
        elif count%4==3:
            #雜訊
            j.append(x)
            count+=1
            xc+=1
        else:
            #最低錄取分數
            x,y=x.split("(")
            score.append(x)
            school.append(school_count)
            score_all.append(x)
            y=y.strip(")")
            score_avg_all.append(y)
            school_all.append(school_count)
            count+=1
            xc+=1
    c+=1

print("school_major=",len(school_major_all))
MinScore_data_df=pd.DataFrame({"UName":school_all,"DName":major_all,"UDName":school_major_all,"MinScore":score_all,"MinScore_avg":score_avg_all})
print(MinScore_data_df)
#比最低錄取分數
for xy in range(len(did_all)):
    if(xy+1==len(did_all)):
        break
    elif MinScore_data_df["UDName"][xy]==MinScore_data_df["UDName"][xy+1]:
        print(MinScore_data_df["UDName"][xy])
        if MinScore_data_df["MinScore"][xy] < MinScore_data_df["MinScore"][xy+1]:
            print(MinScore_data_df["MinScore"][xy])
            MinScore_data_df["MinScore"][xy+1]=" "

        else:
            print(MinScore_data_df["MinScore"][xy+1])
            MinScore_data_df["MinScore"][xy]=" "
            
#刪除較高的最低錄取分數
for xi in range(len(did_all)):
    if MinScore_data_df["MinScore"][xi]==" ":
        MinScore_data_df.drop(xi,inplace=True)
        
print(MinScore_data_df)
MinScore_data_df.to_csv('OutputMin.csv',encoding='utf-8-sig',index=False)
