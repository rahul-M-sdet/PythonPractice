from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radio1 = driver.find_elements(By.XPATH, "//input[@type ='radio']")
print(len(radio1))

for radio2 in radio1:
    if radio2.get_attribute("value") == "radio1":
        radio2.click()
