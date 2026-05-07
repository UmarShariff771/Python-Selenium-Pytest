from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://artoftesting.com/samplesiteforselenium")
action = ActionChains(driver)

# double click
button = driver.find_element(By.ID, "dblClkBtn")
action.double_click(button).perform()
time.sleep(3)

alert = driver.switch_to.alert
print("Alert text is: ", alert.text)
alert.accept()

# context click
action.context_click(button).perform()
time.sleep(3)

driver.quit()
