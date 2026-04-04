import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.positive
def test_valid_login(): #positive
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    username= driver.find_element(By.ID,"user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID,"password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID,"login-button")
    login_button.click()
    assert "inventory" in driver.current_url
    driver.quit()

@pytest.mark.negative
def test_invalid_login(): #negative_testcase
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    print(driver.title)
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_us")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sau")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    assert "inventory" not in driver.current_url
    error = driver.find_element(By.CSS_SELECTOR, ".error > h3").text
    assert "Epic sadface: Username and password do not match any user in this service" in error
    driver.quit()