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