import time

from selenium.webdriver import Chrome

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

time.sleep(8)
driver.maximize_window()
#print(driver.title)
#print(driver.current_url)

driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("malaya")
driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("sahoo")
driver.find_element_by_xpath("//textarea[@rows='3']").send_keys('AT-solapur','\n','PO-Danar','\n','via-manjuri Road')
driver.find_element_by_xpath("//input[@type='email']").send_keys("malaya1122@yahoo.com")
driver.find_element_by_xpath("//input[@type='tel']").send_keys(9090566924)
#  Radioboton
driver.find_element_by_xpath("//input[@value='Male']").click()
driver.find_element_by_xpath("//input[@value='FeMale']").click()