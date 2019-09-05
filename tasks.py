# -*- coding: utf-8 -*-
# @ Author: huangk
# @ Time  : 2019/9/5 14:45

import time
from server import app
from celery.schedules import crontab
from celery.task import periodic_task

@app.task
def subject(i, j):
    print('接收到减法任务')
    time.sleep(1)
    return i - j

@app.task
def sendmail(mail):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'

@periodic_task(run_every=crontab(hour='16', minute='58'))
def schedule_sendmail():
    print('sending mail task')
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'