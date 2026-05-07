from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
# click on alert button

# first alert
driver.find_element(By.ID, "alertButton").click()
alert = driver.switch_to.alert
print("First Alert text is: ", alert.text)
alert.accept()
time.sleep(2)

# second alert
driver.find_element(By.ID, "timerAlertButton").click()
time.sleep(6)
alert = driver.switch_to.alert
print("Second Alert text is: ", alert.text)
alert.accept()
time.sleep(1)

# Third alert cancel
driver.find_element(By.ID, "confirmButton").click()
time.sleep(1)
alert = driver.switch_to.alert
print("Third Alert text is: ", alert.text)
alert.dismiss()
time.sleep(1)

driver.quit()