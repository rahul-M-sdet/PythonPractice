from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("ignore* certification errors")
chrome_options.add_argument("*** start maximized*******")

driver = webdriver.Chrome(executable_path="E:\\New folder (2)\\chromedriver_win32\\chromedriver.exe",options = chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)