# how to provide value into text box
# how to get the status

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

print(driver.title)

# How to find how many inputboxes in web page
inputboxes=driver.find_elements_by_class_name("text_field")
print(len(inputboxes))

driver.find_element_by_id("RESULT_TextField-1").send_keys("malaya")
driver.find_element_by_id("RESULT_TextField-2").send_keys("sahoo")

status=driver.find_element_by_id("RESULT_TextField-1")
print(status.is_displayed())

status=driver.find_element_by_id("RESULT_TextField-2")
print(status.is_enabled())
driver.close()
driver.quit()
