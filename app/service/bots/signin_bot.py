from app.common.config_loader import URL_SIGNIN, XPATH_SIGNIN_CONTENT, XPATH_USER, XPATH_SIGN_DAY
from app.service.chrome_service import url, persist_find_element, move_to_element, find_element
from app.service.processing_service import wait_load, safe_continue

def signin(driver):
    # url(driver, URL_HOYOLAB)
    # wait_load(driver)
    # persist_find_element(driver, XPATH_HOYOLAB)
    # safe_continue(driver)
    # hsr_element = find_element(driver, XPATH_HSR, force=True)
    # move_to_element(driver, hsr_element, click=True)
    # persist_find_element(driver, XPATH_HSR_ACTIVE, force=True)
    # signin_element = find_element(driver, XPATH_SIGNIN, force=True)
    # move_to_element(driver, signin_element, click=True)
    url(driver, URL_SIGNIN)
    wait_load(driver)
    persist_find_element(driver, XPATH_SIGNIN_CONTENT)
    wait_load(driver, wait_time=1)
    user_element = find_element(driver, XPATH_USER, force=True)
    move_to_element(driver, user_element, click=True)
    safe_continue(driver)
    sign_day_element = find_element(driver, XPATH_SIGN_DAY)
    if sign_day_element:
        move_to_element(driver, sign_day_element, click=True)