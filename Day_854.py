
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get(r"YOUR_URL")
range_ = driver.find_element(By.ID, "mySlider")

actions = ActionChains(driver)
movement = 50

while True:
    actions.click_and_hold(range_)
    actions.move_by_offset(movement, 0)
    actions.release()
    actions.perform()
    time.sleep(2)
    movement *= -1

