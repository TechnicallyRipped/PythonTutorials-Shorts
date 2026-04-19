

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(r"D:\Code\Technically_Ripped\sel2.html")

time.sleep(2)

input_box = driver.find_element(By.ID, "myInput")
input_box.clear()

time.sleep(20)

driver.quit()

