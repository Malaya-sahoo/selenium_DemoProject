# Webdriver commands programs
import time

from selenium.webdriver import Chrome
driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(8)
driver.close()
driver.quit()