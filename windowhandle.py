import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r"C:\Users\RAHUL\Downloads\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Windows.html")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
parentwindow = driver.current_window_handle
title1 = driver.title
print(title1)
print(parentwindow)
child = driver.window_handles
for handle in child:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="selenium":
        driver.close()

