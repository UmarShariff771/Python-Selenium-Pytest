import unittest
from selenium import webdriver
from POM.pages.LoginPage import LoginPage


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        login = LoginPage(driver)
        login.enter_username("textuser@yopmail.com")
        login.enter_password("Nothing password")
        login.click_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
