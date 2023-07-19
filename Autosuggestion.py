from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.find_element(By.NAME,"q").send_keys("mobiles phones")
My_list=driver.find_elements(By.XPATH,"//li[@class='Y5N33s']/div")
print("total suggestion are:",len(My_list))
for ele in My_list:
    print("suggestion are", ele.text)
    if ele.text=="5g mobiles":
        print("Record found")
        ele.click()
        break




