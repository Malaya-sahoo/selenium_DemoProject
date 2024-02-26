import time

from selenium.webdriver import Chrome

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_xpath("//*[@id='wizardMainRegionV2']/div/div/div[2]/div/div/ul/li[2]/a").click()
driver.find_element_by_xpath("//button[@type='button']").send_keys("Bhubaneshwar (BBI - Biju Patnaik)")

time.sleep(5)

driver.find_element_by_xpath("//input[@type='text']").send_keys("Bengaluru (BLR - Kempegowda Intl.)")

driver.find_element_by_id("d1-btn").clear()
driver.find_element_by_id("d1-btn").send_keys("Thu, Nov 11")

driver.find_element_by_id("d2-btn").clear()
driver.find_element_by_id("d2-btn").send_keys("Thu, Nov 18")

driver.find_element_by_xpath("//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()