

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get('https://www.bing.com')

search_bar = driver.find_element(By.XPATH, '//*[@id="news"]/a')
time.sleep(2)

search_bar.click()


