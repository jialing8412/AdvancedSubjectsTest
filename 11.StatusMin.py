# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:14:29 2020

@author: jialing
"""

import pandas as pd
import numpy as np

Thisyear=[]
Lastyear=[]
Score=[]
Change=[]
School_name=[]

TL1=[]
TL2=[]
TL3=[]
TL4=[]
TL5=[]
TL6=[]
EW1=[]
EW2=[]
EW3=[]
EW4=[]
EW5=[]
EW6=[]
EW7=[]
EW8=[]
EW9=[]
EW10=[]

last_year_file='科系D-108指考.csv'

conversion_table_file='OutputStatus3.csv'

last_year = pd.read_csv(last_year_file,encoding='ANSI')
conversion_table = pd.read_csv(conversion_table_file,encoding='utf-8')

data = conversion_table.drop_duplicates(['school_name'],'first')
change_school = data['school_name'].tolist()

for xt in range(len(change_school)):
    fliter_c = (conversion_table['school_name'] == change_school[xt])
    fliter_l = (last_year['UName'] == change_school[xt])

    conversion_data = np.array(conversion_table[fliter_c])
    last_year_data = np.array(last_year[fliter_l])

    for x in range(len(conversion_data)):
        for y in range(len(last_year_data)):
            if conversion_data[x][2] == last_year_data[y][3]:
                School_name.append(conversion_data[x][0])
                Thisyear.append(conversion_data[x][1])
                Lastyear.append(last_year_data[y][3])
                Score.append(conversion_data[x][3])
                Change.append(conversion_data[x][4])

                EW1.append(last_year_data[y][25])
                EW2.append(last_year_data[y][26])
                EW3.append(last_year_data[y][27])
                EW4.append(last_year_data[y][28])
                EW5.append(last_year_data[y][29])
                EW6.append(last_year_data[y][30])
                EW7.append(last_year_data[y][31])
                EW8.append(last_year_data[y][32])
                EW9.append(last_year_data[y][33])
                EW10.append(last_year_data[y][34])

df=pd.DataFrame({"UName":School_name,"DName":Thisyear,"last_name":Lastyear,"MinScore":Score,"change":Change,\
                 "EW1":EW1,"EW2":EW2,"EW3":EW3,"EW4":EW4,"EW5":EW5,\
                 "EW6":EW6,"EW7":EW7,"EW8":EW8,"EW9":EW9,"EW10":EW10})

df.to_csv('OutpuStatusMin.csv',encoding='utf-8-sig',index=False)