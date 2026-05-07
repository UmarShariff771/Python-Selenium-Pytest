import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


# Marking this as a positive test case
@pytest.mark.positive
def test_drag_and_drop():
    # Launch Edge browser
    driver = webdriver.Edge()

    # Maximize browser window
    driver.maximize_window()

    # Apply implicit wait of 10 seconds
    driver.implicitly_wait(10)

    # Open the target URL
    driver.get("https://jqueryui.com/droppable/")

    # Locate the iframe containing draggable elements
    drage_drop_Frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

    # Switch Selenium control to iframe
    driver.switch_to.frame(drage_drop_Frame)

    # Create ActionChains object
    actions = ActionChains(driver)

    # Locate draggable white box
    drag_element = driver.find_element(By.ID, "draggable")

    # Locate droppable yellow box
    drop_location = driver.find_element(By.ID, "droppable")

    # Scroll element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", drag_element)

    # Perform drag and drop operation
    actions.drag_and_drop(drag_element, drop_location).perform()

    # Capture drop status text after drag and drop
    drop_status = driver.find_element(By.XPATH, "//div[@id = 'droppable'] / p").text

    # Validate successful drag and drop
    assert "Dropped!" in drop_status

    # Switch back to main webpage
    driver.switch_to.default_content()

    # Close browser
    driver.quit()


# Marking this as a negative test case
@pytest.mark.negative
def test_drag_without_perform():
    # Launch Edge browser
    driver = webdriver.Edge()

    # Maximize browser window
    driver.maximize_window()

    # Apply implicit wait of 10 seconds
    driver.implicitly_wait(10)

    # Open the target URL
    driver.get("https://jqueryui.com/droppable/")

    # Locate iframe containing draggable elements
    drag_drop_frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

    # Switch control to iframe
    driver.switch_to.frame(drag_drop_frame)

    # Create ActionChains object
    actions = ActionChains(driver)

    # Locate draggable element
    drag_element = driver.find_element(By.ID, "draggable")

    # Locate droppable element
    drop_element = driver.find_element(By.ID, "droppable")

    # Drag and drop action is defined NOT executed and perform() method is omitted intentionally
    actions.drag_and_drop(drag_element, drop_element)

    # Capture current drop box text
    drop_status = driver.find_element(By.XPATH, "//div[@id = 'droppable'] / p").text

    # Validate drag and drop did NOT happen
    assert "Drop here" in drop_status

    # Switch back to default webpage
    driver.switch_to.default_content()

    # Close browser
    driver.quit()
