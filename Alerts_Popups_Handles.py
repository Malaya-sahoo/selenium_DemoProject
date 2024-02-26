from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=Chrome(executable_path="C:\\Users\\acer\\OneDrive\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Alerts.html")

driver.maximize_window()
time.sleep(5)

switch=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
alert=driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[1]/a")

actions=ActionChains(driver)
actions.move_to_element(switch).move_to_element(alert).click().perform()

#driver.find_element_by_link_text("Alert with OK & Cancel ").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()
#driver.find_element_by_xpath("//*[@id='CancelTab']/button").click()
driver.find_element_by_link_text("click the button to display a confirm box ")
#driver.switch_to_alert().accept()
driver.close()


#driver.switch_to_alert().accept()
#driver.switch_to_alert().dismiss()

