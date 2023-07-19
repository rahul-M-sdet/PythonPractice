import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj=Service("C:\\Users\\rahul.m\Documents\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(5)
driver.quit()


