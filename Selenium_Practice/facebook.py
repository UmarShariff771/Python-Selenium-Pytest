import time
from selenium import webdriver


driver = webdriver.Chromedriver()
driver.get("https://www.facebook.com/")

time.sleep(5)

driver.find_element(By.XPATH, '//input'[0]).sendkeys("")