from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.get("http://demo.automationtesting.in/Register.html")
# count number of options
month=Select(driver.find_element_by_xpath("//select[@placeholder='Month']"))
print(len(month.options))

#select by visible text
month.select_by_visible_text("March")

# Capture all the month and print as output
all_month=month.options
for month in all_month:
    print(month.text)

#select or Not select
status=driver.find_element_by_xpath("//select[@type='text']").is_selected()
print(status)