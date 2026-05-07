import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# positive test case for valid user
@pytest.mark.positive
def test_valid_user():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")

    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Enter valid credentials
    user_name_field.send_keys("umarshariffu77@gmail.com")
    password_field.send_keys("Testing@123$")
    # Submit login form
    login_btn.click()
    time.sleep(3)

    # Validate successful login by checking URL change
    assert "https://www.guvi.in/" in driver.current_url

    # Verify profile/avatar icon is displayed after login
    avatar_icon = driver.find_elements(By.CSS_SELECTOR, ".account-box-toggler > .gravatar-wrap")
    assert len(avatar_icon) > 0
    assert avatar_icon[0].is_displayed()

    # Close browser
    driver.quit()


# Negative test for invalid user
@pytest.mark.negative
def test_invalid_user():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")

    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Enter invalid email
    user_name_field.send_keys("invalid@gmail.com")
    time.sleep(1)

    # Capture and validate error message
    error = driver.find_element(By.CSS_SELECTOR, "#emailgroup > div.is-invalid").text
    assert "Oh! No profile exists with this Email ID. Click here to Sign Up" in error

    password_field.send_keys("Invalidpassword")
    login_btn.click()
    time.sleep(2)

    # Validate input fields show error state
    username_error_class = user_name_field.get_attribute("class")
    assert "is-invalid" in username_error_class
    password_error_class = password_field.get_attribute("class")
    assert "is-invalid" in password_error_class

    # Validate backend error messages
    username_error = driver.find_element(By.CSS_SELECTOR, "#emailgroup > .invalid-feedback").text
    assert "Incorrect Email or Password" in username_error
    password_error = driver.find_element(By.CSS_SELECTOR, "#passwordGroup > .invalid-feedback").text
    assert "Incorrect Email or Password" in password_error

    # Ensure user is still on login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Close browser
    driver.quit()


# Test with both fields empty
@pytest.mark.negative
def test_empty_input_fields():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")

    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Click without entering any data
    login_btn.click()
    time.sleep(2)

    # Validate both fields show error state
    username_error_class = user_name_field.get_attribute("class")
    assert "is-invalid" in username_error_class
    password_error_class = password_field.get_attribute("class")
    assert "is-invalid" in password_error_class

    # Validate password error message
    password_error = driver.find_element(By.CSS_SELECTOR, "#passwordGroup > .invalid-feedback").text
    assert "Hey, Did you forgot your password? Try again." in password_error

    # Ensure user is still on login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Close browser
    driver.quit()


# Test with empty password
@pytest.mark.negative
def test_empty_password_field():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Enter only username
    user_name_field.send_keys("umarshariffu77@gmail.com")
    login_btn.click()
    time.sleep(2)

    # Validate password field shows error
    password_error_class = password_field.get_attribute("class")
    assert "is-invalid" in password_error_class

    password_error = driver.find_element(By.CSS_SELECTOR, "#passwordGroup > .invalid-feedback").text
    assert "Hey, Did you forgot your password? Try again." in password_error

    # Ensure user is still on login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Close browser
    driver.quit()


# Test with empty username
@pytest.mark.negative
def test_empty_username_field():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Enter only password
    password_field.send_keys("Welcome@123")
    login_btn.click()
    time.sleep(2)

    # Validate username field shows error
    username_error_class = user_name_field.get_attribute("class")
    assert "is-invalid" in username_error_class

    # Ensure user is still on login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Close browser
    driver.quit()


# Test with correct email but wrong password
@pytest.mark.negative
def test_wrong_password():
    # Launch Chrome browser
    driver = webdriver.Chrome()
    # Maximize for better element visibility
    driver.maximize_window()

    # Navigate to home page
    driver.get("https://www.guvi.in/")
    # Click the login button
    driver.find_element(By.ID, "login-btn").click()
    time.sleep(2)

    # Validate navigation to login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Locate input fields and login button
    user_name_field = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-btn")

    # Validate visibility and enabled state of fields
    assert user_name_field.is_displayed()
    assert user_name_field.is_enabled()

    assert password_field.is_displayed()
    assert password_field.is_enabled()

    assert login_btn.is_displayed()
    assert login_btn.is_enabled()

    # Enter valid email but incorrect password
    user_name_field.send_keys("umarshariffu77@gmail.com")
    error = driver.find_element(By.CSS_SELECTOR, "#emailgroup > div.is-invalid").text
    assert error in "Oh! No profile exists with this Email ID. Click here to Sign Up"

    password_field.send_keys("wrongpassword")
    login_btn.click()
    time.sleep(2)

    # Validate both fields marked invalid
    username_error_class = user_name_field.get_attribute("class")
    assert "is-invalid" in username_error_class
    password_error_class = password_field.get_attribute("class")
    assert "is-invalid" in password_error_class

    # Validate error message
    username_error = driver.find_element(By.CSS_SELECTOR, "#emailgroup > .invalid-feedback").text
    assert "Incorrect Email or Password" in username_error
    password_error = driver.find_element(By.CSS_SELECTOR, "#passwordGroup > .invalid-feedback").text
    assert "Incorrect Email or Password" in password_error

    # Ensure still on login page
    assert "https://www.guvi.in/sign-in/" in driver.current_url

    # Close browser
    driver.quit()
