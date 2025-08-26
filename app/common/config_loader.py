import os, sys
from pathlib import Path
from dotenv import load_dotenv

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).resolve().parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

def get_env_path(key):
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Missing environment variable: {key}")
    return BASE_DIR / value

CHROME_PATH = get_env_path("CHROME_PATH")
DRIVER_PATH = get_env_path("CHROMEDRIVER_PATH")
USER_DATA   = get_env_path("USER_DATA_DIR")