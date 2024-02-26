import time

from selenium.webdriver import Chrome


driver=Chrome(executable_path="Absolute Path")

driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)

driver.get("http://websites.milonic.com/newtours.demoaut.com/")
time.sleep(5)
print(driver.title)

driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)