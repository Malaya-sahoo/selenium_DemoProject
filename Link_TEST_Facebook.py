import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome(executable_path="C:\\Users\\acer\\Desktop\\New folder\\chromedriver")

driver.get("https://www.facebook.com/login/")
time.sleep(5)
links=driver.find_elements(By.TAG_NAME,"a")

print(driver.title)
print(driver.current_url)

print(len(links))

for abc in links:
    print(abc.text)
    print("print all the links here : ")

#driver.close()
driver.quit()