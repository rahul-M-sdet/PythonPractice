from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
wondowOpened = driver.window_handles
driver.switch_to.window(wondowOpened[1])
print(driver.find_element(By.LINK_TEXT, "mentor@rahulshettyacademy.com").text)

driver.switch_to.window(wondowOpened[0])
driver.find_element(By.ID, "username").send_keys("Email")
driver.find_element(By.ID, "password").send_keys(1234)
driver.find_element(By.NAME, "signin").click()

