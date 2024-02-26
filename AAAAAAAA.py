from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\chromedriver")
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("javatpoint")

act=ActionChains(driver)
act.send_keys(Keys.ENTER).perform()




