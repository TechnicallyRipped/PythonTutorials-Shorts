
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

box = driver.find_element("name","q")
box.send_keys("Hello World")
time.sleep(2)

box.clear()
time.sleep(2)

box.send_keys("Python")
time.sleep(2)

driver.quit()

































