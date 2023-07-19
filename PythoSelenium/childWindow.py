from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowOpened= driver.window_handles

driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowOpened[0])

assert "Opening a new window" == print(driver.find_element(By.TAG_NAME, "h3").text)