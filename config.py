# -*- coding: utf-8 -*-
# @ Author: huangk
# @ Time  : 2019/9/5 14:55
from celery.schedules import crontab
from datetime import timedelta

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

# 定时任务
# CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERYBEAT_SCHEDULE = {
#     'send-every-30-seconds': {
#         'task': 'tasks.sendmail',
#         'schedule': timedelta(seconds=30), # crontab(minute=16, hour=12)
#         'args': (dict(to='windard@windard.com'), )
#     }
# }
