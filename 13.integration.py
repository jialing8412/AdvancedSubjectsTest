# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 01:33:22 2020

@author: jialing
"""

import pandas as pd
import numpy as np
DID=[]
UName=[]
DName=[]
ELLevel=[]
TL1=[]
TL2=[]
TL3=[]
TL4=[]
TL5=[]
TL6=[]
MinScore=[]
NEW1=[]
NEW2=[]
NEW3=[]
NEW4=[]
NEW5=[]
NEW6=[]
NEW7=[]
NEW8=[]
NEW9=[]
NEW10=[]
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
ExamURL=[]
change=[]

conversion_table_file='OutpuStatusMin.csv'
last_year_file='OutputLastMin.csv'
this_year_file='OutputGR.csv'

last_year = pd.read_csv(last_year_file,encoding='utf-8')
this_year = pd.read_csv(this_year_file,encoding='utf-8')
conversion_table = pd.read_csv(conversion_table_file,encoding='utf-8')

data = this_year.drop_duplicates(['UName'],'first')
change_school = data['UName'].tolist()

for xy in range(len(change_school)):
    fliter_c = (conversion_table['UName'] == change_school[xy])
    fliter_l = (last_year['UName'] == change_school[xy])
    fliter_t = (this_year['UName'] == change_school[xy])

    conversion_data = np.array(conversion_table[fliter_c])
    last_year_data = np.array(last_year[fliter_l])
    this_year_data = np.array(this_year[fliter_t])

    for x in range(len(this_year_data)):
        c=0
        for z in range(len(conversion_data)): 
            this_year_name=this_year_data[x][2]
            if this_year_name == conversion_data[z][1]:
                if str(this_year_data[x][0]).zfill(5) in DID:
                    pass
                elif '公費' in this_year_data[x][2]:
                    pass
                else:
                    DID.append(str(this_year_data[x][0]).zfill(5))
                    UName.append(this_year_data[x][1])
                    DName.append(this_year_data[x][2])
                    ELLevel.append(this_year_data[x][4])
                    TL1.append(this_year_data[x][5])
                    TL2.append(this_year_data[x][6])
                    TL3.append(this_year_data[x][7])
                    TL4.append(this_year_data[x][8])
                    TL5.append(this_year_data[x][9])
                    TL6.append(this_year_data[x][10])
                    NEW1.append(this_year_data[x][11])
                    NEW2.append(this_year_data[x][12])
                    NEW3.append(this_year_data[x][13])
                    NEW4.append(this_year_data[x][14])
                    NEW5.append(this_year_data[x][15])
                    NEW6.append(this_year_data[x][16])
                    NEW7.append(this_year_data[x][17])
                    NEW8.append(this_year_data[x][18])
                    NEW9.append(this_year_data[x][19])
                    NEW10.append(this_year_data[x][20])
                    ExamURL.append(this_year_data[x][21])
                    
                    EW1.append(conversion_data[z][5])
                    EW2.append(conversion_data[z][6])
                    EW3.append(conversion_data[z][7])
                    EW4.append(conversion_data[z][8])
                    EW5.append(conversion_data[z][9])
                    EW6.append(conversion_data[z][10])
                    EW7.append(conversion_data[z][11])
                    EW8.append(conversion_data[z][12])
                    EW9.append(conversion_data[z][13])
                    EW10.append(conversion_data[z][14])
                    MinScore.append(conversion_data[z][3])
                    
                    change.append(conversion_data[z][4])
                    c=1
        for y in range(len(last_year_data)):
            this_year_name=this_year_data[x][2]
            last_year_name=last_year_data[y][3]
            if this_year_name==last_year_name:#今年指考跟去年指考名稱完全相同
                if str(this_year_data[x][0]).zfill(5) in DID:
                    pass
                elif '公費' in this_year_name:
                    pass
                else:
                    this_year_name=str(this_year_name).replace('(公費)','')
                    this_year_name=str(this_year_name).replace('(自費)','')
                    last_year_name=str(last_year_name).replace('(自費)','')
                    last_year_name=str(last_year_name).replace('(公費)','')
                    this_year_name=str(this_year_name).replace('(','')
                    this_year_name=str(this_year_name).replace(')','')
                    last_year_name=str(last_year_name).replace('(','')
                    last_year_name=str(last_year_name).replace(')','')
                    DID.append(str(this_year_data[x][0]).zfill(5))
                    UName.append(this_year_data[x][1])
                    DName.append(this_year_name)
                    ELLevel.append(this_year_data[x][4])
                    TL1.append(this_year_data[x][5])
                    TL2.append(this_year_data[x][6])
                    TL3.append(this_year_data[x][7])
                    TL4.append(this_year_data[x][8])
                    TL5.append(this_year_data[x][9])
                    TL6.append(this_year_data[x][10])
                    NEW1.append(this_year_data[x][11])
                    NEW2.append(this_year_data[x][12])
                    NEW3.append(this_year_data[x][13])
                    NEW4.append(this_year_data[x][14])
                    NEW5.append(this_year_data[x][15])
                    NEW6.append(this_year_data[x][16])
                    NEW7.append(this_year_data[x][17])
                    NEW8.append(this_year_data[x][18])
                    NEW9.append(this_year_data[x][19])
                    NEW10.append(this_year_data[x][20])
                    ExamURL.append(this_year_data[x][21])
                    
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
                    MinScore.append(last_year_data[y][39])
                    
                    change.append('2')
                    c=1
    #            不一樣的話就把括號去除
            else:
                this_year_name=str(this_year_name).replace('(公費)','')
                this_year_name=str(this_year_name).replace('(自費)','')
                last_year_name=str(last_year_name).replace('(自費)','')
                last_year_name=str(last_year_name).replace('(公費)','')
                this_year_name=str(this_year_name).replace('(','')
                this_year_name=str(this_year_name).replace(')','')
                last_year_name=str(last_year_name).replace('(','')
                last_year_name=str(last_year_name).replace(')','')
                if this_year_name==last_year_name:#今年指考跟去年指考名稱完全相同
                    if '自費' in this_year_data[x][2]:
                        if str(this_year_data[x][0]).zfill(5) in DID:
                            pass
                        elif '公費' in this_year_data[x][2]:
                            pass
                        else:
                            DID.append(str(this_year_data[x][0]).zfill(5))
                            UName.append(this_year_data[x][1])
                            DName.append(this_year_data[x][2].replace('(自費)',''))
                            ELLevel.append(this_year_data[x][4])
                            TL1.append(this_year_data[x][5])
                            TL2.append(this_year_data[x][6])
                            TL3.append(this_year_data[x][7])
                            TL4.append(this_year_data[x][8])
                            TL5.append(this_year_data[x][9])
                            TL6.append(this_year_data[x][10])
                            NEW1.append(this_year_data[x][11])
                            NEW2.append(this_year_data[x][12])
                            NEW3.append(this_year_data[x][13])
                            NEW4.append(this_year_data[x][14])
                            NEW5.append(this_year_data[x][15])
                            NEW6.append(this_year_data[x][16])
                            NEW7.append(this_year_data[x][17])
                            NEW8.append(this_year_data[x][18])
                            NEW9.append(this_year_data[x][19])
                            NEW10.append(this_year_data[x][20])
                            ExamURL.append(this_year_data[x][21])
                            
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
                            MinScore.append(last_year_data[y][39])
                            
                            change.append('3')
                            c=1
                    else:
                        if str(this_year_data[x][0]).zfill(5) in DID:
                            pass
                        elif '公費' in this_year_data[x][2]:
                            pass
                        else:
                            DID.append(str(this_year_data[x][0]).zfill(5))
                            UName.append(this_year_data[x][1])
                            DName.append(this_year_data[x][2])
                            ELLevel.append(this_year_data[x][4])
                            TL1.append(this_year_data[x][5])
                            TL2.append(this_year_data[x][6])
                            TL3.append(this_year_data[x][7])
                            TL4.append(this_year_data[x][8])
                            TL5.append(this_year_data[x][9])
                            TL6.append(this_year_data[x][10])
                            NEW1.append(this_year_data[x][11])
                            NEW2.append(this_year_data[x][12])
                            NEW3.append(this_year_data[x][13])
                            NEW4.append(this_year_data[x][14])
                            NEW5.append(this_year_data[x][15])
                            NEW6.append(this_year_data[x][16])
                            NEW7.append(this_year_data[x][17])
                            NEW8.append(this_year_data[x][18])
                            NEW9.append(this_year_data[x][19])
                            NEW10.append(this_year_data[x][20])
                            ExamURL.append(this_year_data[x][21])
                            
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
                            MinScore.append(last_year_data[y][39])
                            
                            change.append('23')
                            c=1
        if c==0:
            if str(this_year_data[x][0]).zfill(5) in DID:
                pass
            elif '公費' in this_year_data[x][2]:
                pass
            else:
                DID.append(str(this_year_data[x][0]).zfill(5))
                UName.append(this_year_data[x][1])
                DName.append(this_year_data[x][2])
                ELLevel.append(this_year_data[x][4])
                TL1.append(this_year_data[x][5])
                TL2.append(this_year_data[x][6])
                TL3.append(this_year_data[x][7])
                TL4.append(this_year_data[x][8])
                TL5.append(this_year_data[x][9])
                TL6.append(this_year_data[x][10])
                NEW1.append(this_year_data[x][11])
                NEW2.append(this_year_data[x][12])
                NEW3.append(this_year_data[x][13])
                NEW4.append(this_year_data[x][14])
                NEW5.append(this_year_data[x][15])
                NEW6.append(this_year_data[x][16])
                NEW7.append(this_year_data[x][17])
                NEW8.append(this_year_data[x][18])
                NEW9.append(this_year_data[x][19])
                NEW10.append(this_year_data[x][20])
                ExamURL.append(this_year_data[x][21])
                
                EW1.append(0)
                EW2.append(0)
                EW3.append(0)
                EW4.append(0)
                EW5.append(0)
                EW6.append(0)
                EW7.append(0)
                EW8.append(0)
                EW9.append(0)
                EW10.append(0)
                MinScore.append(0)
                c=1
                change.append('無資料')
                

df=pd.DataFrame({"DID":DID,"UName":UName,"DName":DName,"ELLevel":ELLevel,"MinScore":MinScore,\
                 "TL1":TL1,"TL2":TL2,"TL3":TL3,"TL4":TL4,"TL5":TL5,"TL6":TL6,
                 "EW1":EW1,"EW2":EW2,"EW3":EW3,"EW4":EW4,"EW5":EW5,\
                 "EW6":EW6,"EW7":EW7,"EW8":EW8,"EW9":EW9,"EW10":EW10,\
                 "NEW1":NEW1,"NEW2":NEW2,"NEW3":NEW3,"NEW4":NEW4,"NEW5":NEW5,\
                 "NEW6":NEW6,"NEW7":NEW7,"NEW8":NEW8,"NEW9":NEW9,"NEW10":NEW10,\
                 "ExamURL":ExamURL,"change":change})
df.to_csv('OutputD.csv',encoding='utf-8-sig',index=False)