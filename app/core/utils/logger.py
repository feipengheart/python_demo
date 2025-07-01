from loguru import logger
import os
from datetime import timedelta
from datetime import datetime
import time

from app.core.utils.datetime_utils import get_date, get_full_timestamp


# 配置日志记录器
def log_config():
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>"
    log_directory = "/opt/AI/app/logs"
    log_directory = os.path.join(log_directory, get_date())
    os.makedirs(log_directory,exist_ok=True)

    logger.remove()  # 移除默认的日志处理器

    # 添加一个每天轮换的日志处理器，保留最近7天的日志文件
    logger.add(
        f"{log_directory}/{{time:YYYY-MM-DD}}.log",
        rotation=timedelta(days=1),  # 每天轮换
        retention=timedelta(days=7),  # 保留最近7天的日志
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <4}</level> | <level>{message}</level> ",
        level="INFO",
    )
    return logger
Logger = log_config()
