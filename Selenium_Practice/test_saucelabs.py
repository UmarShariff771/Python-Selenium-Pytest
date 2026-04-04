import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_validation_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    print(driver.title)
    driver.quit()

def test_Invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("locked_out_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    loginButton = driver.find_element(By.ID, "login-button")
    loginButton.click()
    error = driver.find_element(By.CSS_SELECTOR, ".error > h3").text
    print(error)
    print(driver.title)
    driver.quit()