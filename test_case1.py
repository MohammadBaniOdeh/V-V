import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"firefox_driver/geckodriver.exe"

driver = webdriver.Chrome()#options=chrome_options)
#driver = webdriver.Firefox()

driver.implicitly_wait(0.9)

driver.maximize_window()


url = "https://www.seleniumeasy.com/"
driver.get(url=url)

element = driver.find_element(by=By.ID, value="mc-embedded-subscribe")  # will check the Subscribe button.
element.click()

print("Page title is: ")
print(driver.title)

driver.quit()
