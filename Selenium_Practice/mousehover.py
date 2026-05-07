from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.expandtesting.com/hovers")
action = ActionChains(driver)

img1 = driver.find_element(By.XPATH, "//img[@data-testid='img-user-1']")
img2 = driver.find_element(By.XPATH, "//img[@data-testid='img-user-2']")
img3 = driver.find_element(By.XPATH, "//img[@data-testid='img-user-3']")
driver.execute_script("arguments[0].scrollIntoView();", img1)
action.move_to_element(img1).perform()
time.sleep(3)
action.move_to_element(img2).perform()
time.sleep(3)
action.move_to_element(img3).perform()
time.sleep(3)
driver.quit()