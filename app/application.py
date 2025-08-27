from app.common.config_loader import USER_LIST
from app.service.bots.signin_bot import signin
from app.service.chrome_service import init_chrome
from app.service.logging_service import get_logger


logger = get_logger()

total = len(USER_LIST)
for i, user in enumerate(USER_LIST, start=1):
    driver = init_chrome(user)
    signin(driver)
    logger.info(f"用户 {user} 签到成功！（{i}/{total}）")
    driver.quit()
logger.info("任务完成")