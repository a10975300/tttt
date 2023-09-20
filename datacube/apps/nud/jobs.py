# define tasks
from utils.notification import Notification

def my_task():
    notify = Notification()
    notify.nud_notify_by_email(
        subject="2024 NUD Status Tracking (定时任务测试 = 3分钟发一次.)"
    )
    print('执行任务了')