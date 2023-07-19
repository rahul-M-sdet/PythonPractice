from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "Rahul"
service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Rahul")
driver.find_element(By.ID,"alertbtn").click()
Alert = driver.switch_to.alert
Alertname = Alert.text
print(Alert.text)
assert name in Alertname
Alert.accept()
