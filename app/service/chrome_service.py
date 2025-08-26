from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from app.common.config_loader import CHROME_PATH, DRIVER_PATH, USER_DATA

def get_chrome(user_profile):
    options = Options()
    options.binary_location = str(CHROME_PATH)
    options.add_argument(f"--user-data-dir={USER_DATA}/{user_profile}")

    service = Service(str(DRIVER_PATH))

    driver = webdriver.Chrome(service=service, options=options)

    return driver
