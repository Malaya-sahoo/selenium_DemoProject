from selenium.webdriver import Chrome

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("https://www.amazon.in/")

#driver.execute_script("window.scrollBy(0,1000)"," ")

#phone=driver.find_element_by_xpath("//*[@id='kdHVPwQMyxTSTv6Q8Z5zNw']")
#driver.execute_script("arguments(0),scrollIntoView();",phone)

comp=driver.find_element_by_xpath("//div[@id='8ece6d63-75a2-4de9-9b4a-5ed5da9cd953']")
driver.execute_script("arguments[0],scrollIntoView();",comp)

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#driver.close()

