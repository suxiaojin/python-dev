'''
python3中，通过threading模块提供线程功能。threading模块中有个Thread类，是模块中最主要的线程类。




'''
import time
import threading

def dowaiting():
    print('start waiting:', time.strftime('%H:%M:%S'))
    time.sleep(3)
    print('stop waiting',time.strftime('%H:%M:%S'))

t=threading.Thread(target=dowaiting)
t.start()
time.sleep(1)
print('start job')
print('end job')