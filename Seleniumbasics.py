#webdriver is a class and chrome is the method but, chrom cannot be invoked directly so they have to call driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

obj_service = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=obj_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.forward()
driver.close()
