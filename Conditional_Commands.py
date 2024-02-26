from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

ele=driver.find_element_by_name("txtUsername")
print(ele.is_displayed()) # return true/false based of element status
print(ele.is_enabled())  # return true/false

pwd_ele=driver.find_element_by_name("txtPassword")
print(pwd_ele.is_displayed())  #return true/false based of element status
print(pwd_ele.is_enabled())  # return true/false

ele.send_keys("Admin")
pwd_ele.send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
