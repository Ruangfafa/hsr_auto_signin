import time

from app.service.chrome_service import get_ready_state, find_element, get_url
from app.service.logging_service import get_logger
from app.common.config_loader import ABNORMAL_XPATH_LIST, ABNORMAL_URL_LIST

logger = get_logger()

def wait_load(driver,wait_time=0.5):
    time.sleep(wait_time)
    while True:
        if get_ready_state(driver) == "complete":
            time.sleep(wait_time)
            logger.info("成功加载网页")
            return
        logger.debug("正在等待加载网页...")

def safe_continue(driver):
    abnormal_warning = False
    while (
            any(abnormal_url in get_url(driver) for abnormal_url in ABNORMAL_URL_LIST) or
            any(find_element(driver, xpath, log=False) for xpath in ABNORMAL_XPATH_LIST)
    ):
        if not abnormal_warning:
            logger.warning("正在等待异常处理...")
            abnormal_warning = True
        time.sleep(1)
    if abnormal_warning:
        time.sleep(1)
    logger.info("已通过异常处理")