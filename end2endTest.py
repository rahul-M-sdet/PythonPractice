import time
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[contains(.,'Shop')]").click()
product=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for products in product:
    productName=products.find_element(By.XPATH,"div/h4/a").text
    if productName == "Blackberry":
        products.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CLASS_NAME,"nav-link").click()
driver.find_element(By.CLASS_NAME,"btn").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"validate").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,"India"))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.CLASS_NAME,"checkbox").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text
assert "Success! Thank you!" in successText









