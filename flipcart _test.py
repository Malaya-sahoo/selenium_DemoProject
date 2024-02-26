from selenium.webdriver import Chrome
driver=Chrome(executable_path='C:\\Users\\acer\\Desktop\\New folder\\chromedriver')

driver.get("https://www.flipkart.com/")

driver.find_element_by_xpath("//input[@type='text']").send_keys('malaya@gmail.com')
driver.find_element_by_xpath("//input[@type='password']").send_keys('asde12333')

#driver.close()

