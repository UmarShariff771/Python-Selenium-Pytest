from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://practice.expandtesting.com/checkboxes")
first_checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input")
second_checkbox = driver.find_element(By.XPATH, "//div [@class='form-check'][2] / input")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_checkbox)

# location1 = first_checkbox.location
# size1 = first_checkbox.size
# location2 = second_checkbox.location
# size2 = second_checkbox.size
#
# center_x1 = location1['x'] + size1['width'] / 2
# center_y1 = location1['y'] + size1['height'] / 2
#
# center_x2 = location2['x'] + size2['width'] / 2
# center_y2 = location2['y'] + size2['height'] / 2

# pyautogui.click(center_x1, center_y1)
first_checkbox.click()
time.sleep(2)
# pyautogui.click(center_x2, center_y2)
second_checkbox.click()
time.sleep(2)
driver.quit()