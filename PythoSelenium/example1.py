import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("E:\\New_folder(2)\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")
driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
driver.find_element(By.NAME,"email").send_keys(9916936186)
driver.find_element(By.ID,"continue").click()
driver.find_element(By.LINK_TEXT,'Forgot Password')
driver.find_element(By.XPATH,"//span[@class='icp-nav-link-inner']").click()
