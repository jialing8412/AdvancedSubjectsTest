# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 03:55:55 2020

@author: jialing
"""

import pandas as pd

gr_df = pd.read_csv('OutputD.csv',encoding='utf-8-sig',dtype ='str')
#print(gr_df)
citypp_df = pd.read_csv('OutputGrVsCityPP.csv',encoding='utf-8-sig',dtype ='str')
print(citypp_df)
dd_df = pd.read_csv('OutputGrVsDurl.csv',encoding='utf-8-sig',dtype ='str')
salary_df = pd.read_csv('OutputGrVsSalary.csv',encoding='utf-8-sig',dtype ='str')
print(salary_df)
ud_df = pd.read_csv('OutputGrVsUurl.csv',encoding='utf-8-sig',dtype ='str')
df=pd.merge(gr_df,citypp_df,how='left', on='DID')
df=pd.merge(df,dd_df,how='left', on='DID')
df=pd.merge(df,salary_df,how='left', on='DID')
df=pd.merge(df,ud_df,how='left', on='DID')
df=df.fillna(0) #把NaN資料替換成0 

df = df[["DID","UName","UURL","DName","DURL","Salary","SalaryURL","ELLevel","MinScore",\
                 "TL1","TL2","TL3","TL4","TL5","TL6",\
                 "EW1","EW2","EW3","EW4","EW5","EW6","EW7","EW8","EW9","EW10",\
                 "NEW1","NEW2","NEW3","NEW4","NEW5","NEW6","NEW7","NEW8","NEW9","NEW10",\
                 "City","PP","ExamURL"]] # 调整列顺序

df.to_csv("D.csv", encoding="utf_8_sig",index=False)
