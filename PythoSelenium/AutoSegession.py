import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest').send_keys("ind")
time.sleep

countires = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countires))

for country in countires:
    if country.text == "india":
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute("value") == "india"