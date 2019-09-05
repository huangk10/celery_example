# -*- coding: utf-8 -*-
# @ Author: huangk
# @ Time  : 2019/9/5 14:16

import time
from server import add
from tasks import subject, sendmail

# 一般用法
# print(sendmail.delay(dict(to='celery@python.org')))
answer = sendmail.delay(dict(to='windard@windard.com'))

while 1:
    print('wait for ready')
    if answer.ready():
        break
    time.sleep(0.5)

print(answer.get())


