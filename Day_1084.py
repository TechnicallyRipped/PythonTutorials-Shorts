
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(r"D:\Code\Technically_Ripped\a3.html")

time.sleep(2)
button = driver.find_element(By.ID, "confirmBox")
button.click()

alert = driver.switch_to.alert
time.sleep(2)

alert.accept() #dismiss()

time.sleep(2)

driver.quit()

