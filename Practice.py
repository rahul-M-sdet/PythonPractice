from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.amazon.com/")
driver.maximize_window()

