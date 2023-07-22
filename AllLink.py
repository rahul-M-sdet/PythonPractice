from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")
image = driver.find_elements(By.TAG_NAME,"img")
print(len(image))

for title in image:
    print(title.text)