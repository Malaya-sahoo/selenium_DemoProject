import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("https://en-gb.facebook.com/")
driver.maximize_window()

driver.find_element_by_name('email').send_keys('malaya@12345')
driver.find_element_by_name('pass').send_keys('abcd1234')
#driver.find_element_by_name('login').click()

driver.find_element_by_xpath("//a[text()='Create New Account']").click()
time.sleep(3)

driver.find_element_by_name('firstname').send_keys('Raj')
driver.find_element_by_name('lastname').send_keys('das')
driver.find_element_by_name('reg_email__').send_keys('raj@1234')

day=Select(driver.find_element_by_id('u_2_l_ZB'))
day.select_by_index(27)



