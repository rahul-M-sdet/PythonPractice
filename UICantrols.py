from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

Checkboxes =driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(Checkboxes))

for checkbox in Checkboxes:
    if checkbox.get_attribute("value") == "Option2":
        checkbox.click()
        assert checkbox.is_selected()

        break




