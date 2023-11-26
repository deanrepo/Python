import os
from selenium import webdriver

os.environ['PATH'] += r"D:/Apps/Chromedriver/chrome-win64/chrome-win64"
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(10)
my_element = driver.find_element("ID", "du")
my_element.click()

while(True):
    pass
