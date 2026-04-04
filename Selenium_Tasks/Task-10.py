import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Positive test case: Verify login with valid credentials
@pytest.mark.positive
def test_valid_user_login():
    # Launch Chrome browser and open the website
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Enter valid username and password
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click on login button
    driver.find_element(By.ID, "login-button").click()

    # Capture and validate the title of the webpage
    title = driver.title
    assert "Swag Labs" in title

    # Extract entire webpage content and save to text file
    page_contents = driver.find_element(By.CSS_SELECTOR, "body").text
    write_contents(page_contents)

    # Capture and validate current URL (Inventory page)
    url = driver.current_url
    assert "https://www.saucedemo.com/inventory.html" in url

    # Close the browser
    driver.quit()


# Negative test case: Verify login with invalid username
@pytest.mark.negative
def test_invalid_user_login():
    # Launch browser and open website
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Enter invalid username and valid password
    driver.find_element(By.ID, "user-name").send_keys("non_standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login button
    driver.find_element(By.ID, "login-button").click()

    # Capture and validate error message
    error = driver.find_element(By.CSS_SELECTOR, ".error > h3").text
    assert "Epic sadface: Username and password do not match any user in this service" in error

    # Capture title and URL (for reference)
    title = driver.title
    print(title)
    url = driver.current_url
    print(url)

    # Close the browser
    driver.quit()


# Negative test case: Verify login with locked user
@pytest.mark.negative
def test_locked_user_login():
    # Launch browser and open website
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # Enter locked user credentials
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Click login button
    driver.find_element(By.ID, "login-button").click()

    # Capture and validate error message for locked user
    error = driver.find_element(By.CSS_SELECTOR, ".error > h3").text
    assert "Epic sadface: Sorry, this user has been locked out." in error

    # Capture title and URL (for reference)
    title = driver.title
    print(title)
    url = driver.current_url
    print(url)

    # Close the browser
    driver.quit()


# Function to write webpage content into a text file
def write_contents(text):
    with open("Webpage_task_11.txt", "w") as file:
        file.write(text)
