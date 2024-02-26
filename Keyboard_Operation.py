from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(chromedrivermaneger().install())

#driver=Chrome(executable_path='C:\\Users\\acer\\Desktop\\New folder\\chromedriver')
driver.get("http://demo.automationtesting.in/Register.html")
driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys('Raj')

act=ActionChains(driver)
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()
