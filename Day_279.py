


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

box = driver.find_element("name","q")
box.send_keys("Hello World")
time.sleep(1)

box.send_keys(Keys.ENTER)

