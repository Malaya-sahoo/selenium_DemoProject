from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")
driver.get("https://www.amazon.in/")

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)

#driver.find_element_by_link_text("Mobiles").click()
driver.find_element_by_partial_link_text("Mob").click()
