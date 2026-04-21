

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(r"D:\Code\Technically_Ripped\a2.html")

card = driver.find_element(By.ID, "product-card")

print(f"Class: {card.get_attribute('class')}")
print(f"Data ID: {card.get_attribute('data-id')}")
print(f"Data Cat: {card.get_attribute('data-category')}")









time.sleep(2)