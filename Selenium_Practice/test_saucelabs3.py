# CSS
# Selector
# id =  #
#
# driver.find_element(By.CSS_SELECTOR, "#user-name")
#
#
# class = .
#
#
# driver.find_element(By.CSS_SELECTOR, ".input_error form_input")
#
# tag + attribute
#
# driver.find_element(By.CSS_SELECTOR, "input[name='user-name']")
#
# input[name = 'user-name']


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()
parent_window = driver.current_window_handle
driver.find_element(By.ID, "tabButton").click()
time.sleep(3)
print("New Tab",driver.title)
time.sleep(1)
driver.switch_to.window(parent_window)
print("Parent window", driver.title)
time.sleep(1)
driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.org/")
time.sleep(1)
driver.execute_script("window.open('https://www.facebook.com');")
driver.execute_script("window.open('https://www.instagram.com');")
driver.execute_script("window.open('https://www.saucedemo.com');")

time.sleep(2)

tabs = driver.window_handles

driver.switch_to.window(tabs[0])
print("Google",driver.title)
time.sleep(1)

driver.switch_to.window(tabs[1])
print("Facebook",driver.title)
time.sleep(1)

driver.switch_to.window(tabs[2])
print("Insta",driver.title)
time.sleep(1)

driver.switch_to.window(tabs[3])
print("Saucedemo",driver.title)
time.sleep(1)

driver.switch_to.window(tabs[0])
print("back to Google",driver.title)
time.sleep(1)

driver.quit()







