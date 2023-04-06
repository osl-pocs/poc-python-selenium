# Adds chromedriver binary to path
import chromedriver_binary  # noqa: #F401
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://localhost:18000")
assert "Directory listing for" in driver.title

driver.close()
