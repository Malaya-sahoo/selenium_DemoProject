import time

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath("//input[@type='text']").send_keys('malaya')
driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys('sahoo')
driver.find_element_by_xpath("//textarea[@rows='3']").send_keys('solapur, bhadrak')
driver.find_element_by_xpath("//input[@type='email']").send_keys('sahoo92@gmail.com')
driver.find_element_by_xpath("//input[@type='tel']").send_keys('912487422838')

# checking on radio botton
driver.find_element_by_xpath("//input[@value='Male']").click()

# checking on checkbox
driver.find_element_by_xpath("//input[@value='Movies']").click()

# checking dropdown, we can select value,index,visible_text

skill=Select(driver.find_element_by_xpath("//select[@type='text']"))
#skill=Select(driver.find_element_by_id('Skills'))
skill.select_by_index(9)
#skill.select_by_visible_text("c")

#coun=Select(driver.find_element_by_xpath("//select[@id='country']"))
coun=Select(driver.find_element_by_id('country'))
coun.select_by_index(4)
