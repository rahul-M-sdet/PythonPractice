from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

#service_obj = Service("E:\\New folder (2)\\edgedriver_win32\\edgedriver.exe")

#driver = webdriver.Edge(service=service_obj)

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys('r@gmail.com')
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("hello@1234")
driver.find_element(By.XPATH, "//a[@class ='forgot-password-link']").click()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()



