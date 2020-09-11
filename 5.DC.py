"""
Created on Thu Aug 22 17:06:19 2019

@author: jialing
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://campus4.ncku.edu.tw/uac/cross_search/class_info/index.html'
response = requests.get(url)
response.encoding = 'big5'
soup = BeautifulSoup(response.text,'lxml')
soup.find_all('li')
group_name=[]
web_link=[]
find_g = soup.find("div",class_="g")


for link in find_g.findAll('a'):
    link_a = link.get('href')

    group_name.append(link.get_text().strip(" "))
    web_link.append("https://campus4.ncku.edu.tw/uac/cross_search/class_info"+link_a.strip("."))

first_data_df=pd.DataFrame({"學群":group_name,"連結":web_link})


school_list=[]#存校名
major_list=[]#存科系名
majorgroup_list=[]#存學群
majorclass_list=[]#存學類
count_alldata_list=[]#數所有要的資料的資料數
count_data_list=[]#數加到正確list裡的資料數
no_data_list=[]#確認沒有科系或資料漏掉沒加到list裡
for link in first_data_df["連結"]:
#    print(link)
    url2="https://campus4.ncku.edu.tw/uac/cross_search/class_info/D19.html"
    response = requests.get(link)
    response.encoding = 'big5'
    soup = BeautifulSoup(response.text,'lxml')
    majorgroup = soup.find("h1").get_text()
    data=soup.get_text()

    count=0
    is_want_data=False
    ciy=[]
    all_data=[]
    count_alldata=0
    count_data=0
    for i in data.split("\n\n"):
        for j in i.split("\n"):
            j=j.strip(" ")
#            all_data.append(j)
            count+=1

    #--------------------------------------------------
            if count==431:#從學群的位置開始是我要的資料
                print(j)
                is_want_data=True
            if is_want_data==True:
                if j!="":
                    all_data.append(j)
                    count_alldata+=1
#

    for x in all_data:
        if "學群" in x:
            pass
            count_data+=1
        elif "學類" in x:
#            print(x)
            majorclass = x
            count_data+=1
        elif "大學" in x:
            school = x
            count_data+=1
        elif "醫學院" in x:
            school = x
            count_data+=1
        elif "稻江科技暨管理學院" in x:#如果只用學院會跟科系的學院搞混
            school = x
            count_data+=1
        elif "系" in x:
            count_data+=1
            majorgroup_list.append(majorgroup.strip(" "))
            majorclass_list.append(majorclass)
            school_list.append(school)
            major_list.append(x)
        elif "學院學士班" in x:
            count_data+=1
            majorgroup_list.append(majorgroup.strip(" "))
            majorclass_list.append(majorclass)
            school_list.append(school)
            major_list.append(x)
        elif "學位"in x:
            count_data+=1
            majorgroup_list.append(majorgroup.strip(" "))
            majorclass_list.append(majorclass)
            school_list.append(school)
            major_list.append(x)
        elif "組" in x:
            count_data+=1
            majorgroup_list.append(majorgroup.strip(" "))
            majorclass_list.append(majorclass)
            school_list.append(school)
            major_list.append(x)
        elif "學士班" in x:
            count_data+=1
            majorgroup_list.append(majorgroup.strip(" "))
            majorclass_list.append(majorclass)
            school_list.append(school)
            major_list.append(x)
        else:
            no_data_list.append(x)
        

    count_alldata_list.append(count_alldata)
    count_data_list.append(count_data)

group_df=pd.DataFrame({"Gname":majorgroup_list,"Cname":majorclass_list,"Uname":school_list,"Dname":major_list})

group_df.to_csv('OutputSC.csv',encoding='utf_8_sig',index=False)
cg_df=pd.DataFrame({"Cname":majorclass_list,"Gname":majorgroup_list})

cg_data = cg_df.drop_duplicates(['Cname','Gname'],'first')
cg_data.to_csv('CG.csv',encoding='utf_8_sig',index=False)