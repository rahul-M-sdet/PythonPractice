import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
Excepted = ['Cucumber - 1 kg', 'Raspberry - 1/4 kg', 'Strawberry - 1/4 kg']
service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys("ber")
time.sleep(2)
Items =driver.find_elements(By.XPATH, "//img[@class='product-image']")

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)

assert count > 0
for result in results:
    result




