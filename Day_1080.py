

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(r"D:\Code\Technically_Ripped\sel.html")

time.sleep(1)

input_box = driver.find_element(By.ID, "myInput")
input_box.send_keys("Hello from Selenium!")

time.sleep(20)

driver.quit()

