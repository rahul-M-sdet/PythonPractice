from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BrowserSortedVeggieList  = []
service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH, "//span[text() ='Veg/fruit name' ]").click()
Veggielist= driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in Veggielist:
    BrowserSortedVeggieList.append(ele.text)

orignailBrowserSortedList = BrowserSortedVeggieList.copy()
BrowserSortedVeggieList.sort()



assert orignailBrowserSortedList == BrowserSortedVeggieList
