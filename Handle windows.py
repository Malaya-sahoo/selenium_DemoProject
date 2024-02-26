import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://demo.automationtesting.in/Index.html")
driver.maximize_window()
driver.find_element_by_id("entering").click()
time.sleep(5)


switc=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
alt=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[1]/a")
wind=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[2]/a")

actions=ActionChains(driver)
actions.move_to_element(switc).move_to_element(alt).move_to_element(wind).click().perform()
driver.find_element_by_xpath("//*[@id='dismiss-button']").click()
driver.switch_to_alert().dismiss()

print(driver.current_window_handle())
handles=driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)




