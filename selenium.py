# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# driver = webdriver.Chrome()
# driver.get('https://www.amazon.com')
# driver.maximize_window()
from selenium import webdriver
import chromedriver_binary  # Adds chromedriver binary to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title