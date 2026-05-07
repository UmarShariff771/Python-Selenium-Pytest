from POM.pages.Locators import Locators
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input_field = Locators.username_input_field
        self.password_input_field = Locators.password_input_field
        self.login_button = Locators.login_button

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_input_field).clear()
        self.driver.find_element(By.XPATH, self.username_input_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_input_field).clear()
        self.driver.find_element(By.XPATH, self.password_input_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()