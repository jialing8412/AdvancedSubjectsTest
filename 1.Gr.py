# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 19:21:49 2019

@author: jialing
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

def transform_GSAT(x):
    x1,x2=x.split("≥")
    if x1=="國文":
        if x2=="頂標":
            GSAT_C.append("5")
        elif x2=="前標":
            GSAT_C.append("4")
        elif x2=="均標":
            GSAT_C.append("3")
        elif x2=="後標":
            GSAT_C.append("2")
        elif x2=="底標":
            GSAT_C.append("1")
        else:
            GSAT_C.append("0")
    elif x1=="英文":
        if x2=="頂標":
            GSAT_E.append("5")
        elif x2=="前標":
            GSAT_E.append("4")
        elif x2=="均標":
            GSAT_E.append("3")
        elif x2=="後標":
            GSAT_E.append("2")
        elif x2=="底標":
            GSAT_E.append("1")
        else:
            GSAT_E.append("0")
    elif x1=="數學":
        if x2=="頂標":
            GSAT_M.append("5")
        elif x2=="前標":
            GSAT_M.append("4")
        elif x2=="均標":
            GSAT_M.append("3")
        elif x2=="後標":
            GSAT_M.append("2")
        elif x2=="底標":
            GSAT_M.append("1")
        else:
            GSAT_M.append("0")
    elif x1=="自然":
        if x2=="頂標":
            GSAT_N.append("5")
        elif x2=="前標":
            GSAT_N.append("4")
        elif x2=="均標":
            GSAT_N.append("3")
        elif x2=="後標":
            GSAT_N.append("2")
        elif x2=="底標":
            GSAT_N.append("1")
        else:
            GSAT_N.append("0")
    elif x1=="社會":
        if x2=="頂標":
            GSAT_S.append("5")
        elif x2=="前標":
            GSAT_S.append("4")
        elif x2=="均標":
            GSAT_S.append("3")
        elif x2=="後標":
            GSAT_S.append("2")
        elif x2=="底標":
            GSAT_S.append("1")
        else:
            GSAT_S.append("0")
    elif x1=="英聽":
        x2=x2.strip("級")
        GSAT_EL.append(x2)
    else:
        GSAT_EL.append("0")

url = 'https://university-tw.ldkrsi.men/uac/#gsc.tab=0'
response = requests.get(url) 
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
soup.find_all('li') 

school_name=[]
school_web=[]
for link in soup.findAll('a'):
    link_a = link.get('href')

    if str.isdigit(link_a):
        name=link.get_text()
        school_name.append(name)
        web='https://university-tw.ldkrsi.men/uac/'+str(link_a)+'#gsc.tab=0'#把單個網頁兜起來
        school_web.append(web)

school_data_df=pd.DataFrame({"school_name":school_name,"school_web":school_web})



matrix=[]
DID=[]#存放代碼
DNAME=[]#存放科系
UNAME=[]#學校名稱
UDNAME=[]
GSAT=[]#存放學測
GSAT_C=[]#學測國文
GSAT_E=[]#學測英文
GSAT_M=[]#學測數學
GSAT_N=[]#學測自然
GSAT_S=[]#學測社會
GSAT_A=[]#學測總級分
GSAT_EL=[]#學測英聽
CHIN=[]#國
EN=[]#英
MA1=[]#數甲
MA2=[]#數乙
PY=[]#物
CH=[]#化
BI=[]#生
HI=[]#歷
GE=[]#地
CI=[]#公
DID_link=[]
x=0

for n in school_data_df.school_web:
    url2="https://university-tw.ldkrsi.men/uac/006#gsc.tab=0"
    r2 = requests.get(n)
    soup = BeautifulSoup(r2.text,"lxml")
    count=0
    sel_td = soup.select('td')
    shool_title = soup.find('h1')  #抓網頁的 h1(校名)
    ti = shool_title.text  #抓出校名的文字
    ti = ti.strip("109年")
    ti = ti.strip("指考分發")
    for link_a in soup.findAll('a'):
        link_href = link_a.get('href')
        we="https://campus4.ncku.edu.tw/uac/cross_search/dept_info/"
        if we in  link_href:
            DID_link.append(link_href)

    for data in sel_td :
        matrix.append(data.text)#把資料放進陣列裡
        count+=1
        for x in data :
            if count % 13  == 1 :#校系代碼
                DID.append(data.text)
            if count % 13  == 2 :#科系名稱
                DNAME.append(x)
                UNAME.append(ti)
                UDNAME.append(ti+" "+x)
            if count % 13  == 3 :#學測標準
                #學測 5:頂標; 4: 前標; 3: 均標; 2: 後標; 1: 底標; 0:未採計
                #英聽 只有一個英文字母: A, B, C, F，N:未採計
                GSAT.append(data.text)
#                print(len(x))
                #學測標準是--的
                if x=="--":
                    GSAT_C.append("0")#學測國文
                    GSAT_E.append("0")#學測英文
                    GSAT_M.append("0")#學測數學
                    GSAT_N.append("0")#學測自然
                    GSAT_S.append("0")#學測社會
                    GSAT_A.append("0")#學測總級分
                    GSAT_EL.append("N")#學測英聽
                elif "≥" in x:
                    if "國文" not in x:
                        GSAT_C.append("0")#學測國文
                    if "英文" not in x:
                        GSAT_E.append("0")#學測英文
                    if "數學" not in x:
                        GSAT_M.append("0")#學測數學
                    if "自然" not in x:
                        GSAT_N.append("0")#學測自然
                    if "社會" not in x:
                        GSAT_S.append("0")#學測社會
                    if "總級分" not in x:
                        GSAT_A.append("0")#學測總級分
                    if "英聽" not in x:
                        GSAT_EL.append("N")#學測英聽
                    if "、" in x:
                        n=len(x)//5
#                        print("x=",x)
                        x1=x.split("、",n)
                        for i in range(n):
                            transform_GSAT(x1[i])#換算成學測個別

                    else:
                        transform_GSAT(x)#換算成學測個別
            if count % 13  == 4 :
                x=x.strip("x")
                if x=="--":
                    CHIN.append("0")
                else:
                    CHIN.append(x)
            if count % 13  == 5 :
                x=x.strip("x")
                if x=="--":
                    EN.append("0")
                else:
                    EN.append(x)
            if count % 13  == 6 :
                x=x.strip("x")
                if x=="--":
                    MA1.append("0")
                else:
                    MA1.append(x)
            if count % 13  == 7 :
                x=x.strip("x")
                if x=="--":
                    MA2.append("0")
                else:
                    MA2.append(x)
            if count % 13  == 8 :
                x=x.strip("x")
                if x=="--":
                    PY.append("0")
                else:
                    PY.append(x)
            if count % 13  == 9 :
                x=x.strip("x")
                if x=="--":
                    CH.append("0")
                else:
                    CH.append(x)
            if count % 13  == 10 :
                x=x.strip("x")
                if x=="--":
                    BI.append("0")
                else:
                    BI.append(x)
            if count % 13  == 11 :
                x=x.strip("x")
                if x=="--":
                    HI.append("0")
                else:
                    HI.append(x)
            if count % 13  == 12 :
                x=x.strip("x")
                if x=="--":
                    GE.append("0")
                else:
                    GE.append(x)
            if count % 13  == 0 :
                x=x.strip("x")
                if x=="--":
                    CI.append("0")
                else:
                    CI.append(x)

GR_data_df=pd.DataFrame({"DID":DID,"UName":UNAME,"DName":DNAME,\
                             "UDNAME":UDNAME,"ELLevel":GSAT_EL,\
                             "TL1":GSAT_C,"TL2":GSAT_E,"TL3":GSAT_M,\
                             "TL4":GSAT_S,"TL5":GSAT_N,"TL6":GSAT_A,\
                             "NEW1":CHIN,"NEW2":EN,"NEW3":MA1,"NEW4":MA2,\
                             "NEW5":HI,"NEW6":GE,"NEW7":CI,"NEW8":PY,\
                             "NEW9":CH,"NEW10":BI,"ExamURL":DID_link})

GR_data_df.to_csv('OutputGR.csv',encoding='utf-8-sig',index=False)