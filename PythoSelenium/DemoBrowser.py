from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by

#service_obj = Service("E:\\New folder (2)\\edgedriver_win32\\edgedriver.exe")

#driver = webdriver.Edge(service=service_obj)

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
driver.get("https://rahulshettyacademy.com/angularpractice")




