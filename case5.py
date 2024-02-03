import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

service = ChromeService()
os.environ['PATH'] += r"CHROME_DRIVER"

#chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)
#chrome_options.headless = True

driver = webdriver.Chrome()#options=chrome_options)
url = "https://www.seleniumeasy.com/"
driver.get(url=url)

element = driver.find_element(by=By.ID, value="mc-embedded-subscribe")  # will check the Subscribe button.
element.click()

driver.quit()