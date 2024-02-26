#capture all the options and print as output
# count number of options

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("http://demo.automationtesting.in/Register.html")

year=Select(driver.find_element_by_id("yearbox"))
#year.select_by_index(5)
#print(len(year.options))
all_option=year.options
for year in all_option:
    print(year.text)