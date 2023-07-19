import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys("ber")
time.sleep(2)

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)

assert count > 0
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"//tr/td[5]/p")
sum =0
for price in prices:
    sum = sum + int(price.text)

print(sum)
totalAmount = int(driver.find_elements(By.CSS_SELECTOR,".totAmt"))
assert sum == totalAmount

discountAmt = driver.find_elements(By.CSS_SELECTOR,".discountAmt")
assert discountAmt > totalAmount

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

