from datetime import datetime

def get_full_timestamp():
    """
    获取完整的带毫秒的时间戳（年月日时分秒毫秒）
    返回格式为：2025-04-14 12:34:56.789
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S%f")[:-3]  # 毫秒是微秒的前3位
    return timestamp

def get_date():
    """
    获取年月日
    返回格式为：2025-04-14
    """
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date