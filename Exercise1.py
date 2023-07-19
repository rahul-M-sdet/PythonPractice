import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.NAME,"ctl00_mainContent_ddl_originStation1_CTXT").send_keys("BLR")
driver.find_element(By.CSS_SELECTOR,"a[text='Bengaluru (BLR)']").click()
driver.find_element(By.XPATH,"//input[@id='ctl00_mainContent_ddl_destinationStation1_CTXT']").send_keys("DEL")
#wait2 = WebDriverWait(driver, 10)
#wait2.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT," Delhi (DEL)")))
time.sleep(5)
driver.find_element(By.CSS_SELECTOR



