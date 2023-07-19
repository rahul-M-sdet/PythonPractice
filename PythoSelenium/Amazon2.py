import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\\New_folder(2)\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://api.nasa.gov/")
driver.find_element(By.CLASS_NAME,"form-control").send_keys("Rahul")
