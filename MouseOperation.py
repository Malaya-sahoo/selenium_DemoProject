from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys


#driver=Chrome(executable_path='C:\\Users\\acer\\Desktop\\New folder\\chromedriver')
driver.get('http://demo.automationtesting.in/Index.html')
act=ActionChains(driver)

act.click().perform()
act.click(driver.find_element_by_id('btn1')).perform()

#context click(right click)
act.context_click().perform()
act.context_click(driver.find_element_by_id('btn1')).perform()

#act.double_click().perform()
#act.double_click(driver.find_element_by_id('btn1')).perform()
