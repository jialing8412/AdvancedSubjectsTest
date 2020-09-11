# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:52:54 2020

@author: jialing
"""
import pandas as pd
import tabula

file_path='https://www.uac.edu.tw/109data/109DEPchange.pdf'

pdf = tabula.read_pdf(file_path, encoding='utf-8', pages='all')

add_data_df=pd.DataFrame({"校碼":pdf[0]['校碼'],"學校名稱":pdf[0]['學校名稱'],"系組名稱":pdf[0]['系組名稱']})
data0_df=pd.DataFrame({"校碼":pdf[2]['校碼'].str.replace('\r', ''),"校名":pdf[2]['校名'].str.replace('\r', ''),"109招生系組名稱":pdf[2]['109招生系組名稱'].str.replace('\r', ''),"108學年度原系組名稱":pdf[2]['108學年度原系組名稱'].str.replace('\r', '')})
data1_df=pd.DataFrame({"校碼":pdf[3]['校碼'].str.replace('\r', ''),"校名":pdf[3]['校名'].str.replace('\r', ''),"109招生系組名稱":pdf[3]['109招生系組名稱'].str.replace('\r', ''),"108學年度原系組名稱":pdf[3]['108學年度原系組名稱'].str.replace('\r', '')})
data2_df=pd.DataFrame({"校碼":pdf[4]['校碼'].str.replace('\r', ''),"校名":pdf[4]['校名'].str.replace('\r', ''),"109招生系組名稱":pdf[4]['109招生系組名稱'].str.replace('\r', ''),"108學年度原系組名稱":pdf[4]['108學年度原系組名稱'].str.replace('\r', '')})
data3_df=pd.DataFrame({"校碼":pdf[5]['校碼'].str.replace('\r', ''),"校名":pdf[5]['校名'].str.replace('\r', ''),"109招生系組名稱":pdf[5]['109招生系組名稱'].str.replace('\r', ''),"108學年度原系組名稱":pdf[5]['108學年度原系組名稱'].str.replace('\r', '')})

df=pd.concat([data0_df,data1_df,data2_df,data3_df])

df.to_csv("OutputStatus.csv", encoding="utf_8_sig",index=False)