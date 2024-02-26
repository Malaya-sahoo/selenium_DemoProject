from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())

driver.get("www.google.co.in")
driver.maximize_window()

#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(ChromeDriverManager().install())
