

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://google.com")

WebDriverWait(driver, 20).until(
    EC.url_to_be("https://www.instagram.com/")
)

signup_span = driver.find_element(By.XPATH,"//span[text()='Sign up']")
signup_span.click()

time.sleep(5)
print("Website has loaded correctly!")
