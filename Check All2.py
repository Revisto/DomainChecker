from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
from selenium.webdriver.common.keys import Keys
import selenium
from time import time
import random
from URLS2 import URLS
def FreeOrFullDomain(Domain,Drive):
    B=time()
    
    Url="https://iranic.com/"
    Drive.get(Url)
    Type=Drive.find_element_by_class_name("bigtxt")
    Type.send_keys(Domain)
    Type.send_keys(Keys.ENTER)
    try :
        Drive.find_element_by_class_name("red")
        #Drive.quit()
        print (time()-B)
        return False
    except:
        #Drive.quit()
        print (time()-B)
        return True

    
Free=[]
count=0
Path="/usr/lib/chromium-browser/chromedriver"
drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
for Url in URLS:
    count+=1
    print(count)
    if FreeOrFullDomain(Url+".ir",drive):
        print (Url+".ir")
        Free.append(Url+".ir")
        print (Free)
        with open("FREES2.py","w") as f:
            f.write(str(Free))