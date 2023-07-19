from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.find_element(By.NAME,"proceed").click()
alt=driver.switch_to.alert
alt_txt=alt.text
print("The alert text is:",alt_txt)
alt.accept()
driver.find_element(By.ID,"login1").send_keys("rahul")
driver.close()