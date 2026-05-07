import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
def test_validate_locators():
    # Launch Edge browser
    driver = webdriver.Edge()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")

    # Base element (anchor)
    element = driver.find_element(By.XPATH, "(//div[@id='solutions'])[1]")

    # Parent using axis
    parent = element.find_element(By.XPATH, "parent::div")

    # First child of parent
    first_child = parent.find_element(By.XPATH, "child::*[1]")

    # Second sibling (your working logic)
    second_sibling = driver.find_element(
        By.XPATH,
        "(//div[@id='solutions'])[1]/parent::div/following-sibling::div[1]"
    )

    # Ancestors
    ancestors = element.find_elements(By.XPATH, "ancestor::*")

    # Following siblings
    following_siblings = parent.find_elements(By.XPATH, "following-sibling::div")

    # Preceding elements
    preceding_elements = driver.find_elements(By.XPATH,
                                              "(//div[@id='solutions'])[5] / parent::div / preceding-sibling::*")

    # Parent of first element having href
    parent_of_href = driver.find_element(By.XPATH, "//link[@href]/parent::*")

    # Assertions
    assert element is not None
    assert parent is not None
    assert first_child is not None
    assert second_sibling is not None
    assert len(ancestors) > 0
    assert len(following_siblings) > 0
    assert len(preceding_elements) > 0
    assert parent_of_href is not None

    # Basic Interactions
    first_child.click()
    second_sibling.click()

    # Close the browser
    driver.quit()
