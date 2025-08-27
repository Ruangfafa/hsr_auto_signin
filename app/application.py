from app.common.config_loader import USER_LIST
from app.service.signin_bot import signin
from app.service.chrome_service import init_chrome
from app.service.logging_service import get_logger

logger = get_logger()

def main():
    total = len(USER_LIST)
    for i, user in enumerate(USER_LIST, start=1):
        driver = init_chrome(user)
        try:
            signin(driver)
            logger.info(f"用户 {user} 签到成功！（{i}/{total}）")
        except Exception as e:
            logger.error(f"用户 {user} 签到失败：{e}", exc_info=True)
        finally:
            driver.quit()
    logger.info("任务完成")

if __name__ == "__main__":
    main()
