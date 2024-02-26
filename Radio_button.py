import time

from selenium.webdriver import Chrome

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

driver.maximize_window()

print(driver.find_element_by_name("RESULT_RadioButton-7").is_selected())

driver.find_element_by_name("RESULT_RadioButton-7").click()
driver.find_element_by_xpath("//input[@value='Radio-0']").click()
#driver.find_element_by_id("RESULT_RadioButton-7_0").click()

print(driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected())
