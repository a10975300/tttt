from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from nud.jobs import my_task

class NudConfig(AppConfig):
    name = 'nud'
    verbose_name = 'NUD'
    orderIndex = 2

    def ready(self):
        # Start the scheduler when the Django application is ready
        scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)
        scheduler.add_job(my_task, 'interval', minutes=30)  # 添加定时任务 seconds
        scheduler.start()