# Adds chromedriver binary to path
import chromedriver_binary  # noqa: #F401
from chromedriver_binary import chromedriver_filename
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option(
    "prefs", {"intl.accept_languages": "en,en_US"}
)
driver = webdriver.Chrome(
    options=chrome_options,
    executable_path=chromedriver_filename,
)

driver.get("http://localhost:18000")
assert "Directory listing for" in driver.title

driver.close()
