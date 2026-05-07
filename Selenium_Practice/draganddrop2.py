from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.expandtesting.com/drag-and-drop")
actions = ActionChains(driver)

try:
    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")

    driver.execute_script("arguments[0].scrollIntoView(true);", source)

    try:
        actions.click_and_hold(source).pause(1).move_to_element(target).pause(1).release().perform()
        print("Drag and drop performed successfully")
    except (ElementClickInterceptedException, ElementNotInteractableException, MoveTargetOutOfBoundsException) as e:
        print("Error occurred while performing drag and drop:", e)

#
#         time.sleep(5)
except TimeoutException:
    print("Element not found within the specified time")
except Exception as e:
    print("An unexpected error occurred:", str(e))
finally:
    print("Test completed, closing the browser.")
    driver.quit()

