# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:02:56 2020

@author: jialing
"""

import pandas as pd
import numpy as np

gr_file = 'OutputGR.csv'
dd_file = 'OutputDURL.csv'

DID=[]
UName=[]
DName=[]
link=[]

s=[]

noDID=[]
noUName=[]
noDName=[]
noCname=[]

dd = pd.read_csv(dd_file,encoding='ANSI')
gr = pd.read_csv(gr_file,encoding='utf-8')

data = gr.drop_duplicates(['UName'],'first')
change_school = data['UName'].tolist()
print(change_school[37])
for xy in range(len(change_school)):
    fliter_g = (gr['UName'] == change_school[xy])
    fliter_d = dd['科系名稱'].str.contains(str(change_school[xy]))
    #不要忘记正则表达式的写法，'.'在里面要用'\.'表示
    
    dd_data = np.array(dd[fliter_d])
    gr_data = np.array(gr[fliter_g])
    
    for a in range(len(gr_data)):
        for b in range(len(dd_data)):
            if str(gr_data[a][1]+gr_data[a][2])==dd_data[b][1]:
                if str(gr_data[a][0]).zfill(5) in DID:
                    pass
                else:
                    DID.append(str(gr_data[a][0]).zfill(5))
                    UName.append(gr_data[a][1])
                    DName.append(gr_data[a][2])
                    link.append(dd_data[b][2])
                    s.append('all')
            else:
                gr_name=str(gr_data[a][1]+gr_data[a][2]).replace("(","")
                gr_name=gr_name.replace(")","")
                gr_name=gr_name.replace("臺北","台北")
    #            print(gr_name)
                dd_name=str(dd_data[b][1]).replace("(","")
                dd_name=dd_name.replace(")","")
                dd_name=dd_name.replace("臺北","台北")
                if gr_name==dd_name:
                    if str(gr_data[a][0]).zfill(5) in DID:
                        pass
                    else:
                        DID.append(str(gr_data[a][0]).zfill(5))
                        UName.append(gr_data[a][1])
                        DName.append(gr_data[a][2])
                        link.append(dd_data[b][2])
                        s.append('all-')
                else:
                    gr_name=gr_name.replace("學系","學系 ")
                    gr_name=gr_name.split(' ')
                    gr_name=gr_name[0]
                    if gr_name==dd_name:
                        if str(gr_data[a][0]).zfill(5) in DID:
                            pass
                        else:
                            DID.append(str(gr_data[a][0]).zfill(5))
                            UName.append(gr_data[a][1])
                            DName.append(gr_data[a][2])
                            link.append(dd_data[b][2])
                            s.append('all-+')
                    else:
                        if gr_name[:10]==dd_name[:10]:
                            print(gr_name[:10])
                            if str(gr_data[a][0]).zfill(5) in DID:
                                pass
                            else:
                                DID.append(str(gr_data[a][0]).zfill(5))
                                UName.append(gr_data[a][1])
                                DName.append(gr_data[a][2])
                                link.append(dd_data[b][2])
                                s.append('----')

                        
#data_df=pd.DataFrame({"DID":DID,"UName":UName,"DName":DName,"DURL":link,"s":s})
#data_df.to_csv('OutputGrVsDURL_test.csv',encoding='utf-8-sig',index=False)
data_df=pd.DataFrame({"DID":DID,"DURL":link})
data_df.to_csv('OutputGrVsDURL.csv',encoding='utf-8-sig',index=False)