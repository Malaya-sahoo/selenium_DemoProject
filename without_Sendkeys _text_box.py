import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select


driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

driver.maximize_window()
time.sleep(5)

skills=Select(driver.find_element_by_id("Skills"))
skills.select_by_value("Android")

#print(len(skills.options))
skill=(len(skills.options))
a=skills.options
for skills in a:
    print(skills.text)


