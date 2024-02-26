from selenium.webdriver import Chrome

driver=Chrome(executable_path="C:\\Users\\acer\\OneDrive\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

print(driver.find_element_by_xpath("//input[@value='Male']").is_selected())

driver.find_element_by_xpath("//input[@value='Male']").click()

print(driver.find_element_by_xpath("//input[@value='Male']").is_selected())


driver.close()