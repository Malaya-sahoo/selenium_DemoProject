from selenium.webdriver import Chrome
driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

driver.maximize_window()

driver.find_element_by_id("checkbox1").click()
#driver.find_element_by_xpath("//input[@value='Movies']").click()
driver.find_element_by_id("checkbox3").click()
driver.find_element_by_id("checkbox2").click()
 
