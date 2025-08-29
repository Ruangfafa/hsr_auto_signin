import os, sys
from pathlib import Path
from dotenv import load_dotenv

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")

def get_env_path(key):
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Missing environment variable: {key}")
    return BASE_DIR / value

CHROME_PATH = get_env_path("CHROME_PATH")
DRIVER_PATH = get_env_path("CHROMEDRIVER_PATH")
USER_DATA   = get_env_path("USER_DATA_DIR")

URL_HOYOLAB = os.getenv("URL_HOYOLAB")
URL_SIGNIN = os.getenv("URL_SIGNIN")

# XPATH_HOYOLAB = os.getenv("XPATH_HOYOLAB")
# XPATH_HSR = os.getenv("XPATH_HSR")
# XPATH_HSR_ACTIVE = os.getenv("XPATH_HSR_ACTIVE")
# XPATH_SIGNIN = os.getenv("XPATH_SIGNIN")

XPATH_SIGNIN_CONTENT = os.getenv("XPATH_SIGNIN_CONTENT")
XPATH_USER = os.getenv("XPATH_USER")
XPATH_SIGN_DAY = os.getenv("XPATH_SIGN_DAY")
XPATH_REWARD = os.getenv("XPATH_REWARD")

abnormal_xpath = os.getenv("ABNORMAL_XPATH")
ABNORMAL_XPATH_LIST = abnormal_xpath.split("_;_") if abnormal_xpath else []

abnormal_url = os.getenv("ABNORMAL_URL")
ABNORMAL_URL_LIST = abnormal_url.split("_;_") if abnormal_url else []

user_list = os.getenv("USER_LIST")
USER_LIST = user_list.split("_;_") if user_list else []