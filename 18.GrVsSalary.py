# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:41:17 2020

@author: jialing
"""
import pandas as pd
import numpy as np

gr_file = 'OutputGR.csv'
salary_fire = 'OutputSalary.csv'

DID=[]
School=[]
Major=[]
SalaryURL=[]
Salary=[]
s=[]
noDID=[]
noSchool=[]
noMajor=[]
noSalaryURL=[]
noSalary=[]

salary = pd.read_csv(salary_fire,encoding='utf-8')
gr = pd.read_csv(gr_file,encoding='utf-8')


data = gr.drop_duplicates(['UName'],'first')
change_school = data['UName'].tolist()
#print(change_school)
#print(change_school[37])
school_name=[]
major_name=[]
link=[]
major_salary=[]

#print(salary['school_name'])
for x in range(len(salary)):
    if '科技大學' in salary['school_name'][x]:
        pass
    else:
        sname = salary['school_name'][x].replace("私立","")
        sname = sname.replace("(淡水工商)","")#真理大學
        sname = sname.replace("(臺中健管)","")#亞洲大學
        school_name.append(sname.strip())
        major_name.append(salary['major_name'][x])
        link.append(salary['major_link'][x])
        major_salary.append(salary['salary'][x])
#    print(salary['school_name'][x])
salary104=pd.DataFrame({"school_name":school_name,"major_name":major_name,\
                        "link":link,"salary":major_salary})
did=[]
uname=[]
dname=[]
for y in range(len(gr)):
    mname=gr['DName'][y].replace("學系","學系 ")
    mname=mname.split(" ")[0]
    did.append(gr['DID'][y])
    uname.append(gr['UName'][y])
    dname.append(mname.strip())
gr_new=pd.DataFrame({"DID":did,"UName":uname,"DName":dname})
for xy in range(len(change_school)):
    fliter_s = (salary104['school_name'] == change_school[xy])
    fliter_g = (gr_new['UName'] == change_school[xy])
    
    salary104_data = np.array(salary104[fliter_s])
    gr_data = np.array(gr_new[fliter_g])
    
    
    #print(gr[fliter_g])
    print(salary104[fliter_s])
    for a in range(len(gr_data)):
        for b in range(len(salary104_data)):
            if gr_data[a][1]==salary104_data[b][0]:#如果學校一樣
                if gr_data[a][2]==salary104_data[b][1]:
                    if str(gr_data[a][0]).zfill(5) in DID:
                        pass
                    else:
                        DID.append(str(gr_data[a][0]).zfill(5))
                        School.append(gr_data[a][1])
                        Major.append(gr_data[a][2])
                        SalaryURL.append(salary104_data[b][2])
                        Salary.append(salary104_data[b][3])
                        s.append('all')
                elif gr_data[a][2]=="歷史學系":
                    if salary104_data[b][1]=="史學系":
                        if str(gr_data[a][0]).zfill(5) in DID:
                            pass
                        else:
                            DID.append(str(gr_data[a][0]).zfill(5))
                            School.append(gr_data[a][1])
                            Major.append(gr_data[a][2])
                            SalaryURL.append(salary104_data[b][2])
                            Salary.append(salary104_data[b][3])
                            s.append('史')
                elif gr_data[a][2]=="中國語文學系"or gr_data[a][2]=="中國文學系" or gr_data[a][2]=="中國文學學系":
                    if salary104_data[b][1]== "國文學系":
                        if str(gr_data[a][0]).zfill(5) in DID:
                            pass
                        else:
                            DID.append(str(gr_data[a][0]).zfill(5))
                            School.append(gr_data[a][1])
                            Major.append(gr_data[a][2])
                            SalaryURL.append(salary104_data[b][2])
                            Salary.append(salary104_data[b][3])
                            s.append('中')
                
                elif gr_data[a][2][:3] == salary104_data[b][1][:3]:
                    if str(gr_data[a][0]).zfill(5) in DID:
                        pass
                    else:
                        DID.append(str(gr_data[a][0]).zfill(5))
                        School.append(gr_data[a][1])
                        Major.append(gr_data[a][2])
                        SalaryURL.append(salary104_data[b][2])
                        Salary.append(salary104_data[b][3])
                        s.append('o')

data_df=pd.DataFrame({"DID":DID,"gr_fi_school":School,"gr_fi_major":Major,\
                 "SalaryURL":SalaryURL,"Salary":Salary,"s":s})
data_df.to_csv('OutputGrVsSalary_0712.csv',encoding='utf-8-sig',index=False)#
#no_data_df=pd.DataFrame({"DID":noDID,"UName":noSchool,"DName":noMajor,\
#                 "SalaryURL":noSalaryURL,"Salary":noSalary,})
#no_data_df.to_csv('OutputGrVsSalary_test_no.csv',encoding='utf-8-sig',index=False)#