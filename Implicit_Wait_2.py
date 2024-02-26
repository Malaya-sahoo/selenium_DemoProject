from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)

print("implicit Wait Example")

ele=driver.find_element_by_name("q")
ele.send_keys("javatpoint")
driver.close()


