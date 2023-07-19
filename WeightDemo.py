import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
ExpectedList = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actualList = []
service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
Results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(Results)
for result in Results:
    result.find_element(By.XPATH,"div/button").click()
    actualList.append(result.find_element(By.XPATH,"h4").text)
assert  actualList == ExpectedList
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
Prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
sum = 0
for price in Prices:
    sum = sum + int(price.text)
print(sum)
TotalAmount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == TotalAmount
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)
Discount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(Discount)
assert Discount < TotalAmount







