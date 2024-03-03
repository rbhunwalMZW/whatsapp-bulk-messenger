from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")

driver = webdriver.Chrome(DRIVER_BIN)
driver.get("https://www.python.org")

print(driver.title)

driver.close()