from selenium import webdriver
driver=webdriver.Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.implicitly_wait(10)


driver.get("https://www.facebook.com/")
driver.find_element_by_name("email").send_keys("malaya92@gmail.com")
driver.find_element_by_name("pass").send_keys("malaya1234")

print(driver.title)

driver.find_element_by_name("login").click()