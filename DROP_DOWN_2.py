from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()

drop=Select(driver.find_element_by_id("Skills"))

#select by Value
#drop.select_by_value("Adobe InDesign")

#select by visible text
drop.select_by_visible_text("Android")

# Select by index
#drop.select_by_index(7)

# count number of Options

print(len(drop.options))

# Capture all the Options and print them as  Output

all_option=drop.options

for option in all_option:
    print(option.text)