from _ast import Assert

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#service_obj = Service("E:\\New folder (2)\\edgedriver_win32\\edgedriver.exe")

#driver = webdriver.Edge(service=service_obj)

service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
driver.implicitly_wait(10)
#driver.get("https://rahulshettyacademy.com/angularpractice")
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(20)
#driver.find_element(By.NAME, "name").send_keys("Rahul")
driver.implicitly_wait(10)
#driver.find_element(By.NAME, "email").send_keys("87rhlmishra@gmail.com")
driver.implicitly_wait(20)
#driver.find_element(By.ID, "exampleInputPassword1").send_keys(1234)
driver.implicitly_wait(20)
#driver.find_element(By.ID, "exampleCheck1").click()
driver.implicitly_wait(20)

#xpath tagname[@attributename=value
#css selector tagname[attributename=value]
#

#//input[@type = submit
#driver.find_element(By.XPATH , "//input[@type = 'submit']").click()
#message = driver.find_element(By.CLASS_NAME, "alert-success").text
#print(message)
#assert "Success" in message
#driver.find_element(By.XPATH, "//input[@type='text'][3]").send_keys("Hellorahul")

# static dropdown
#dropdown =Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_index(0)

Dropdown = Select(driver.find_element(By.CLASS_NAME, "form-control"))
Dropdown.select_by_value("Student")

