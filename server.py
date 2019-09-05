# -*- coding: utf-8 -*-
# @ Author: huangk
# @ Time  : 2019/9/5 14:15

from __future__ import absolute_import, unicode_literals
from celery import Celery
import time

# app = Celery('server',
#              broker='redis://127.0.0.1:6379/0',
#              backend='redis://127.0.0.1:6379/0',
#              include=['tasks'])
#
# app.conf.update(result_expires=3600)
app = Celery('server', include=['tasks'])
app.config_from_object('config')
# app.autodiscover_tasks(['celery_example.task'])

@app.task
def add(x, y):
    print("计算2个值的和: %s %s" % (x, y))
    return x + y

@app.task
def upper(v):
    for i in range(10):
        time.sleep(1)
        print(i)
    return v.upper()



if __name__ == '__main__':
    """
    普通任务： `celery -A server worker -l info`
    调度任务： `celery -A server beat -l info`
    """
    app.start()
