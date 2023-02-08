from datetime import datetime


def get_date_time_now():
    now = datetime.now()
    time_now = now.strftime("%d/%m/%Y %H:%M:%S")
    return time_now