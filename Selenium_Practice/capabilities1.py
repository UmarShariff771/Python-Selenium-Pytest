# # import pytest
# # from selenium import webdriver


# # @pytest.fixture
# # def setup():
# #     #setup code
# #     driver = webdriver.Chrome()
# #     driver.maximize_window()
# #     yield driver
# #     #teardown code
# #     driver.quit()

# # @pytest.mark.smoke
# # def test_google(setup):
# #     driver = setup
# #     driver.get("https://www.google.com/")
# #     print("Title of the page is: ", driver.title)
# #     assert "Google" in driver.title


# # def test_amazon(setup):
# #     driver = setup
# #     driver.get("https://www.amazon.in/")
# #     print("Title of the page is: ", driver.title)
# #     assert "Amazon" in driver.title


# # # fixture
# from selenium import webdriver

# options = webdriver.FirefoxOptions()
# options.add_argument("--start-maximized")

# driver = webdriver.Firefox(options=options)
# driver.get("https://www.saucedemo.com")

# driver.quit()

# 1.
# Browser
# control
# API
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
# driver.quit()
#
# 2.
# Element
# control
# API
# driver.find_element(By.ID, "user-name") \
#     driver.find_element(By.XPATH, "//input[@id='password']")
#
# 3.
# Action
# APIs
# element = driver.find_element(By.ID, "user-name")
# element.send_keys("standard_user")
# element = driver.find_element(By.XPATH, "//input[@id='password']")
# element.click()
#
# 4.
# Validation
# APIs
# element = driver.find_element(By.ID, "user-name")
# element.text
# element.is_displayed()
# element.is_enabled()
#
# Chrome > webdriver.Chrome()

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com")

capabilities = {
    "browserName": "chrome",
    "browserVersion": "114.0",
    "platformName": "Windows 10", }
