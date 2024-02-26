from selenium import webdriver

driver=webdriver.Chrome(executable_path='C:\\Users\\acer\\Desktop\\New folder\\chromedriver')
driver.get('http://demo.automationtesting.in/Register.html')

driver.maximize_window()
# checking CheakBox
# you can take xpath and id ,its does not matter
driver.find_element_by_xpath("//input[@value='Movies']").click()
driver.find_element_by_id('checkbox1').click() 