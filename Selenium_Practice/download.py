from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os

download_path = os.path.join(os.getcwd(), "chromedownloads")
os.makedirs(download_path, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://practice.expandtesting.com/download")
time.sleep(3)
link =driver.find_element(By.LINK_TEXT,"1775220960873_DNDAgentFile.txt")
print(link.text)
driver.execute_script("arguments[0].scrollIntoView(true);", link)
time.sleep(2)
driver.execute_script("arguments[0].click();", link)
time.sleep(5)
print("File downloaded successfully to: ", download_path)
time.sleep(5)
driver.quit()
