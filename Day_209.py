



# pip install selenium
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(60)

driver.quit()

































