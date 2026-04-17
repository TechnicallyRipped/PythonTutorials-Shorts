

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opts = Options()
opts.add_argument("--log-level=3") 

driver = Chrome(options=opts)

driver.get('https://technicallyripped.com/checks.html')

button1 = driver.find_element(By.CLASS_NAME,'check2')

if button1.is_selected():
    print('It is checked')
else:
    print('It is NOT checked')
