import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("E:\\New_folder(2)\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://api.nasa.gov/")
time.sleep(5)
driver.find_element(By.ID,"user_first_name").send_keys("rahul")
driver.find_element(By.ID,"user_last_name").send_keys("Mishra")
driver.find_element(By.NAME,"user[email]").send_keys("87rhlmishra@gmail.com")

