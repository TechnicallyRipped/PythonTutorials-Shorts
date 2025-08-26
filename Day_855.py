
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("URL_PATH")

dropdown = Select(driver.find_element("id", "fruitSelect"))

while True:
    dropdown.select_by_visible_text("Banana")
    time.sleep(2)
    dropdown.select_by_value("apple")
    time.sleep(2)
    dropdown.select_by_index(2)
    time.sleep(2)

