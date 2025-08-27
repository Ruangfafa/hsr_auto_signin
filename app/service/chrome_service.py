import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from app.common.config_loader import CHROME_PATH, DRIVER_PATH, USER_DATA
from app.service.logging_service import get_logger

logger = get_logger()

def init_chrome(user_profile):
    try:
        options = Options()
        options.binary_location = str(CHROME_PATH)
        options.add_argument(f"--user-data-dir={USER_DATA}/{user_profile}")

        service = Service(str(DRIVER_PATH))

        driver = webdriver.Chrome(service=service, options=options)

        logger.info(f"Chrome 实例启动成功: {user_profile}")
        return driver

    except Exception as e:
        logger.error(f"启动 Chrome 失败 (profile={user_profile}): {e}", exc_info=True)
        sys.exit(1)

def url(driver, url):
    try:
        driver.get(url)
        logger.info(f"成功打开 URL: {url}")

    except Exception as e:
        logger.error(f"打开 URL 失败: {url} -> {e}", exc_info=True)
        sys.exit(1)

def get_url(driver):
    try:
        url = driver.current_url
        logger.info(f"成功获取当前URL：{url}")
        return url
    except Exception as e:
        logger.error(f"无法获取当前URL：{e}", exc_info=True)
        sys.exit(1)

def get_ready_state(driver):
    try:
        ready_state = driver.execute_script("return document.readyState")
        logger.debug(f"成功获取网页状态：{ready_state}")
        return ready_state
    except Exception as e:
        logger.error(f"无法获取网页状态：{e}", exc_info=True)
        sys.exit(1)

def find_element(driver, xpath, force=False, log=True):
    try:
        element = driver.find_element(By.XPATH, xpath)
        if log:
            logger.info(f"成功获取【元素】：{xpath}")
        return element
    except Exception as e:
        if log:
            logger.info(f"无法获取【元素】：{xpath}")
        if force:
            logger.error(f"无法获取【元素】：{xpath} -> {e}", exc_info=True)
            sys.exit(1)
        return None

def find_elements(driver, xpath, force=False, log=True):
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        if log:
            logger.info(f"成功获取【元素列表】：{xpath}")
        return elements
    except Exception as e:
        if log:
            logger.info(f"无法获取【元素列表】：{xpath}")
        if force:
            logger.error(f"无法获取【元素列表】：{xpath} -> {e}", exc_info=True)
            sys.exit(1)
        return None

def persist_find_element(driver, xpath, tryout=5, force=False):
    for i in range(tryout):
        element = find_element(driver, xpath, log=False)
        if element:
            logger.info(f"成功找到【元素】：{xpath}")
            return element
        logger.info(f"正在尝试寻找【元素】：{xpath}（尝试{i + 1}/{tryout}）")
        time.sleep(1)
    logger.info(f"无法找到【元素】：{xpath} ")
    if force:
        logger.error(f"无法找到【元素】：{xpath} ")
        sys.exit(1)
    return None

def persist_find_elements(driver, xpath, tryout=5, force=False):
    for i in range(tryout):
        elements = find_elements(driver, xpath, log=False)
        if elements:
            logger.info(f"成功找到【元素列表】：{xpath}")
            return elements
        logger.info(f"正在尝试寻找【元素列表】：{xpath}（尝试{i + 1}/{tryout}）")
        time.sleep(1)
    logger.info(f"无法找到【元素列表】：{xpath} ")
    if force:
        logger.error(f"无法找到【元素列表】：{xpath} ")
        sys.exit(1)
    return None

def move_to_element(driver, element, click=False):
    try:
        hover_script = """
                var ev = new MouseEvent('mouseover', {
                    bubbles: true,
                    cancelable: true,
                    view: window
                });
                arguments[0].dispatchEvent(ev);
                """
        driver.execute_script(hover_script, element)
        logger.info("成功触发【元素】的 mouseover")
        if click:
            driver.execute_script("arguments[0].click();", element)
            logger.info("成功点击指定【元素】")
    except Exception as e:
        logger.error(f"模拟光标动作失败：{e}", exc_info=True)