from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
from selenium.webdriver.common.keys import Keys
import selenium
import time
import random

def FreeOrFullDomain(Domain):
    Path="/usr/lib/chromium-browser/chromedriver"
    Drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
    Url="https://iranic.com/"
    Drive.get(Url)
    Type=Drive.find_element_by_class_name("bigtxt")
    Type.send_keys(Domain)
    Type.send_keys(Keys.ENTER)
    try :
        Drive.find_element_by_class_name("red")
        return False
    except:
        return True
    Drive.quit()
    
    