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

driver.get("https://www.saucedemo.com")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(3)
first_image = driver.find_element(By.XPATH, "//div[@class='inventory_item'][1]//img")

location = first_image.location
size = first_image.size

center_x = location['x'] + size['width'] / 2
center_y = location['y'] + size['height'] / 2

# pyautogui.rightClick(center_x, center_y)
pyautogui.click(center_x, center_y, button='right') # Right-click the mouse at the center of the first image
time.sleep(2)

pyautogui.press("down", presses = 3)  # Press the down arrow key to navigate the context menu
pyautogui.press("enter")  # Press the enter key to select the "Save image as..." option
time.sleep(2)  # Wait for the "Save As" dialog to open
pyautogui.write("first_image.png")  # Type the desired file name for the image
time.sleep(3)  # Wait for a moment before pressing enter
pyautogui.press("enter")  # Press the enter key to save the image
time.sleep(10)
driver.quit()
