



from selenium.webdriver import Chrome
import time

driver = Chrome()

driver.get('https://www.google.com')
driver.get('https://www.bing.com')

for i in range(100):
    
    driver.back()
    time.sleep(2)

    driver.forward()
    time.sleep(2)















