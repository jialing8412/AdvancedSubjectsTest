# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:23:06 2020

@author: jialing
"""
import pandas as pd
import numpy as np

thisyear=[]
lastyear=[]
score=[]
change=[]
school_name=[]

last_year_file='科系D-108指考.csv'
conversion_table_file='OutputStatus2.csv'
min_score_file = 'OutputMin.csv'

last_year = pd.read_csv(last_year_file,encoding='ANSI')
conversion_table = pd.read_csv(conversion_table_file,encoding='utf-8')
min_score = pd.read_csv(min_score_file,encoding='utf-8')


data = conversion_table.drop_duplicates(['校名'],'first')
change_school = data['校名'].tolist()

def comp(conversion_data,last_year_data,min_score_data):
    last_name=[]
    last_min=[]

    for x in range(len(last_year_data)):
        for y in range(len(min_score_data)):

            if last_year_data[x][3] == min_score_data[y][1]:
                
                last_name.append(last_year_data[x][3])
                last_min.append(min_score_data[y][3])
    
    min_df=pd.DataFrame({"last_name":last_name,"last_min":last_min})
    data_score=[]
    score_c=[]
    min_sc=0
    x=0

    for x in range(len(conversion_data)):
        for y in range(len(min_df)):
            if x!=len(conversion_data):
                if conversion_data[x][4]=='更名':
                    if conversion_data[x][3] == min_df['last_name'][y]:
                        school_name.append(conversion_data[x][1])
                        thisyear.append(conversion_data[x][2])
                        lastyear.append(min_df['last_name'][y])
                        score.append(min_df['last_min'][y])
                        change.append('更名')
                if conversion_data[x][4]=='分組':
                    if conversion_data[x][3]== min_df['last_name'][y]:
                        school_name.append(conversion_data[x][1])
                        thisyear.append(conversion_data[x][2])
                        lastyear.append(min_df['last_name'][y])
                        score.append(min_df['last_min'][y])
                        change.append('分組')
                if conversion_data[x][4]=='合併':#如果狀態是合併
                    if conversion_data[x][3]== min_df['last_name'][y]:#如果科系一樣
                        if x+1!=len(conversion_data):
                            if conversion_data[x][2]==conversion_data[x+1][2]:#代表這行跟下行是一樣的
                                if conversion_data[x][2] in data_score: #如果新校名已存
                                    score_c.append(float(min_df['last_min'][y]))
                                else:
                                    score_c.append(float(min_df['last_min'][y]))
                                    data_score.append(conversion_data[x][2])
                            else:
                                data_score=[]
                                score_c.append(float(min_df['last_min'][y]))
                                min_sc = min(score_c)
                                school_name.append(conversion_data[x][1])
                                thisyear.append(conversion_data[x][2])
                                lastyear.append(min_df['last_name'][y])
                                score.append(min_sc)
                                change.append('合併')
                                score_c=[]

for xy in range(len(change_school)):
    fliter_c = (conversion_table['校名'] == change_school[xy])
    fliter_l = (last_year['UName'] == change_school[xy])
    fliter_m = (min_score['UName'] == change_school[xy])
    
    conversion_data = np.array(conversion_table[fliter_c])
    last_year_data = np.array(last_year[fliter_l])
    min_score_data = np.array(min_score[fliter_m])
    comp(conversion_data,last_year_data,min_score_data)

df=pd.DataFrame({"school_name":school_name,"thisyear":thisyear,"last_name":lastyear,"score":score,"change":change})
df.to_csv('OutputStatus3.csv',encoding='utf-8-sig',index=False)