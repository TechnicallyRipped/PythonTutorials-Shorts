
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

# Open a new tab using JavaScript
driver.execute_script("window.open('', '_blank');") 
# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

driver.get('https://bing.com')

for i in range(100):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)














