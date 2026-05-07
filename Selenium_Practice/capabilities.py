import time

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
# from selenium.webdriver.firefox.options import Options

# Chrome capabilities
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--ignore-certificate-errors")
# chrome_options.add_argument("--disable-popup-blocking")

# Edge capabilities
edge_options = Options()
edge_options.add_argument("--start-maximized")
edge_options.add_argument("-inprivate")
edge_options.add_argument("--disable-notifications")
edge_options.add_argument("--ignore-certificate-errors")
edge_options.add_argument("--disable-popup-blocking")

# Firefox capabilities
# firefox_options = Options()
# firefox_options.add_argument("--private")
# firefox_options.set_preference("dom.webnotifications.enabled", False)  # Disable notifications
# firefox_options.set_preference("dom.disable_open_during_load", True)  # Disable popups
# firefox_options.set_preference("acceptInsecureCerts", True)  # Ignore SSL
# firefox_options.add_argument("--start-maximized")
# driver.set_window_size(1920, 1080)


# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Edge(options=edge_options)
# driver = webdriver.Firefox(options=firefox_options)
driver.get("https://www.saucedemo.com")
time.sleep(5)
driver.quit()