import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome(executable_path="C:\\Users\\acer\\Downloads\\chromedriver_win32\\chromedriver")
driver.get("https://www.facebook.com")

# Maximize Browser
driver.maximize_window()

# enter data into the TextCase
driver.find_element(By.XPATH,"//a[text()='Create New Account']").click()

time.sleep(3)

driver.find_element(By.NAME,"firstname").send_keys("hello")
driver.find_element(By.NAME,"lastname").send_keys("sahoo")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("malayaxyz@yahoo.com")

#driver.close()