from selenium import webdriver;
from time import sleep;
import pandas;


finalDepartmentUrls = [];
departmentNames = [];

browser = webdriver.Chrome();


browser.get("https://collego.ceec.edu.tw/Highschool/School");
elements_schoolNames = browser.find_elements_by_xpath("//div[@id='box_collegeList']/div/a[@class='box__item']");    #擷取含有學校名稱的元素

schoolNames = [];
for i in range(len(elements_schoolNames)):
    schoolNames.append(elements_schoolNames[i].text);

for schoolName in schoolNames:
    url = "https://collego.ceec.edu.tw/Login/Search?t=" + schoolName;
    browser.get(url);
    sleep(2);
    
    scrollHeight = 0;
    scrollHeightNext = 1;
    while scrollHeight < scrollHeightNext:
        scrollHeight = browser.execute_script("return document.body.scrollHeight");
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);");
        sleep(1);
        scrollHeightNext = browser.execute_script("return document.body.scrollHeight");
    
    elements_department = browser.find_elements_by_xpath("//div[@class='scard well well-add-card']/a");
    
    departmentUrls = [];
    for i in range(len(elements_department)):
        if "DepartmentIntro" in elements_department[i].get_property("href"):
            departmentNames.append(elements_department[i].text);
            departmentUrls.append(elements_department[i].get_property("href"));
    
    for departmentUrl in departmentUrls: 
        url = departmentUrl;
        browser.get(url);
        elements_finalDepartmentUrl = browser.find_elements_by_xpath("//a[@style='padding-left:15px;']");
        departmentUrlcurrentCount = len(finalDepartmentUrls);
        for i in range(len(elements_finalDepartmentUrl)):
            if ".edu.tw" in elements_finalDepartmentUrl[i].get_property("href"):
                finalDepartmentUrls.append(elements_finalDepartmentUrl[i].get_property("href"));
        
        if departmentUrlcurrentCount == len(finalDepartmentUrls):
            finalDepartmentUrls.append("0");
        
browser.close();

csv_content = {"科系名稱" : departmentNames,
               "科系網址" : finalDepartmentUrls};

csv_content_df = pandas.DataFrame(csv_content);
csv_content_df.to_csv("OutputDURL.csv", encoding="utf_8_sig");

