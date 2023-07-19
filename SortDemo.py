from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
BrowserVeggieList =[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[(text()='Veg/fruit name')]").click()
VeggiesList = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in VeggiesList:
    BrowserVeggieList.append(ele.text)
OrignalBrowserSortedList = BrowserVeggieList.copy()

BrowserVeggieList.sort()

assert BrowserVeggieList == OrignalBrowserSortedList





