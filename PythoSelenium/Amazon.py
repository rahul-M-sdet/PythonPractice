import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service("E:\\New_folder(2)\\chromedriver_win32\\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.find_element(By.LINK_TEXT,"Sell").click()
driver.find_element(By.CLASS_NAME,"hm-icon-label").click()
time.sleep(5)
action=ActionChains(driver)










