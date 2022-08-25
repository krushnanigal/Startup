from lib2to3.pgen2 import driver
import pandas as pd

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service

url = pd.read_html("https://startuptalky.com/indian-startups-funding-investors-data-2022/")
path =r'C:\Users\Code\Downloads\edgedriver_win64\msedgedriver'
optios=Options()
optios.binary_location =r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
optios.add_argument(r"user-data-dir=C:\Users\Code\AppData\Local\Microsoft\Edge\User Data")
optios.add_argument('profile-directory=Profile 1')
# optios.add_argument("--no-sandbox")
optios.add_experimental_option("detach", True)


ser=Service(executable_path=path)
browser=webdriver.Edge(service=ser,options=optios)
# browser.get("https://startuptalky.com/indian-startups-funding-investors-data-2022/")
# print(len(url))
# print(url[0].iloc[:,0])

for i in url:
    firstCol=i.iloc[:,0]
    for i in firstCol:
        browser.switch_to.new_window('tab')
        browser.get("https://www.google.com/search?q={}+careers".format(i))    
        containsText=browser.find_element(by="xpath",value='//div[@class="jtfYYd"]/div/div[contains(text(),carrer)or contains(text(),carrers)]/a').click()
        #f'//div[@class="jtfYYd"]/div/div[contains(text(),{i})or contains(text(),carrers)]/a'
        print(i)
    


#//div[@class="jtfYYd"]/div/div[contains(text(),karix) or contains(text(),carrers)]/a
# print(containsText)


# print(firstCol)
# print(sfsdf[0][sfsdf[0].columns[0]])
browser.quit()
