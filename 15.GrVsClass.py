# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:28:49 2020

@author: jialing
"""
import pandas as pd
import numpy as np

gr_file = 'OutputGR.csv'
sc_fire = 'OutputSC.csv'

DID=[]
UName=[]
DName=[]
Cname=[]

s=[]

noDID=[]
noUName=[]
noDName=[]
noCname=[]

sc = pd.read_csv(sc_fire,encoding='utf-8')
gr = pd.read_csv(gr_file,encoding='utf-8')

data = gr.drop_duplicates(['UName'],'first')
change_school = data['UName'].tolist()
print(change_school[37])
for xy in range(len(change_school)):
    fliter_s = (sc['Uname'] == change_school[xy])
    fliter_g = (gr['UName'] == change_school[xy])
    
    sc_data = np.array(sc[fliter_s])
    gr_data = np.array(gr[fliter_g])
    
#    print(sc_data)
    for a in range(len(gr_data)):
        for b in range(len(sc_data)):
            if gr_data[a][1]==sc_data[b][2]:#如果學校一樣
                if gr_data[a][2]==sc_data[b][3]:
                    if str(gr_data[a][0]).zfill(5) in DID:
                        pass
                    else:
                        DID.append(str(gr_data[a][0]).zfill(5))
                        UName.append(gr_data[a][1])
                        DName.append(gr_data[a][2])
                        Cname.append(sc_data[b][1])
                    
data_df=pd.DataFrame({"DID":DID,"Cname":Cname})
data_df.to_csv('DC.csv',encoding='utf-8-sig',index=False)