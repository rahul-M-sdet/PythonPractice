import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://paytm.com/")
driver.maximize_window()

#driver.switch_to.frame("document")
#src= driver.find_element(By.XPATH,"//div[@id='draggable']")
# src = driver.find_element(By.XPATH,"//span[text()='Occasional Furniture']")
# dest = driver.find_element(By.XPATH,"//span[text()='Kids Storage']")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT,"Paytm For Business")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Consumer Payments")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Online Payments")).perform()
driver.find_element(By.LINK_TEXT,"Paytm For Business").click()
# time.sleep(5)
# action.drag_and_drop(src,dest).perform()
# time.sleep(5)
# action.double_click(driver.find_element(By.XPATH,"//span[text()='Furniture']")).perform()


