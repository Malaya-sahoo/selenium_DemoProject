import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

s=Service("C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver=webdriver.Chrome('C:\\Users\\acer\\Desktop\\New folder\\chromedriver')
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//a[text()='Create New Account']").click()

time.sleep(3)
driver.find_element_by_name('firstname').send_keys("MALAYA")
driver.find_element_by_class_name("inputtext _58mg _5dba _2ph-").send_keys('SAHOO')
driver.find_element_by_xpath("//input[@type='text']").send_keys('raj@1234gmail.com')
driver.find_element_by_xpath("//input[@type=password]").send_keys('abcd1234')
day=Select(driver.find_element_by_xpath("//select[@name='birthday_day']"))
day.select_by_visible_text("10")
month=Select(driver.find_element_by_name("birthday_month"))
month.select_by_visible_text("October")
year=Select(driver.find_element_by_id("year"))
year.select_by_visible_text("1992")
# radio botton
driver.find_element_by_xpath("//label[text()='Female']").click()


