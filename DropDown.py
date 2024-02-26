from selenium.webdriver import Chrome
#from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=Chrome(executable_path='C:\\Users\\acer\\Desktop\\New folder\\chromedriver')
driver.get("http://demo.automationtesting.in/Register.html")

driver.maximize_window()

#skill=Select(driver.find_element_by_xpath("//select[@type='text']"))
#skill.select_by_index(10)
#skill.select_by_value("Python")
#skill.select_by_visible_text("AutoCAD")


skill=Select(driver.find_element_by_id('Skills'))
#skill.select_by_value("AutoCAD")
#skill.select_by_index(4)
skill.select_by_visible_text("C")

#  Check DOB DropDown
year=Select(driver.find_element_by_id('yearbox'))
year.select_by_value('1990')

mon=Select(driver.find_element_by_xpath("//select[@placeholder='Month']"))
mon.select_by_visible_text("January")

day=Select(driver.find_element_by_id('daybox'))
day.select_by_index(18)

driver.find_element_by_id('firstpassword').send_keys('malaya@1234')
driver.find_element_by_id('secondpassword').send_keys('malaya@1234')
