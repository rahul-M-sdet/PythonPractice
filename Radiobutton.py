from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

Radiobuttons =driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(Radiobuttons))

for radio in Radiobuttons:
    if radio.get_attribute("value") == "radio2":
        radio.click()
        assert radio.is_selected()

        break
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"displayed-text").click()
