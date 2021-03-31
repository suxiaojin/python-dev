'''
python3中，通过threading模块提供线程功能。threading模块中有个Thread类，是模块中最主要的线程类。


from threading import Thread
创建一个线程
t=Tread(target=function_name,args=(function_parameter1,function_parameterN))
t.start


function_name: 需要线程去执行的方法名
args: 线程执行方法接收的参数，该属性是一个元祖，即使只有一个参数也需要在末尾加逗号


'''
2. 使用继承类创建

from threading import Thread
#创建一个类，必须继承Thread
class MyThread(Thread):

    def __init__(self,parameter1):
        #需要执行父类的初始化方法
        Thread.__init__(self)
        #如果有参数，可以封装在类里面
        self.parameter1=parameter1

    # 继承Thread类，需要实现run方法，线程就是从这个方法开始
    def run(self):
        #具体的逻辑
        function_name(self.parameter1)

#如果有参数，实例化的时候需要把参数传递进去
t=MyThread(parameter1)
#使用start启动线程
t.start()
#join方法是 子线程结束之后，主线程再关闭
t.join()


3.线程之间通信 Queue
    ----多个线程之间的通信，声明一个全局的存储对象。所有的线程都调用这一个对象来进行数据的存和取，这样就做到了线程之间的通信。

4.线程事件通知
    休眠 ----wait()
    唤醒-----set()
    清除 ----clear()

from threading import Event,Thread
#接收一个Event对象
def test_event(e):
    print('run....')                                #-----1
    #让这个线程进入休眠
    e.wait()                                        #-----2
    #当线程被唤醒之后，会输出下面的语句
    print('end....')                               #-----5
e=Event()
t=Thread(target=test_event,args=(e,))
#这里会看到输出run...
t.start()
print('set Event...')                              #-----3
#唤醒线程end...
e.set()                                            #-----4








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

import threading
from threading import Thread
import time

g_num=10
def tfunc():
    global g_num
    thread_info=threading.current_thread()
    g_num+=1
    print('call thread func:', threading.get_ident(),thread_info.getName(),g_num)
t=Thread(target=tfunc,name='thread1')
t.start()
tfunc()
t.join()