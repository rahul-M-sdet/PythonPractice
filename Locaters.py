from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj_service = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=obj_service)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("rahul")
driver.find_element(By.NAME,"email").send_keys("87rhlmishra@gmail.com")
driver.find_element(By.ID,"exampleFormControlSelect1").click()
driver.find_element(By.ID,"inlineRadio1").click()
#statis drop down

Dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
Dropdown.select_by_index(0)
Dropdown.select_by_visible_text("Female")

driver.find_element(By.CLASS_NAME,"btn-success")
