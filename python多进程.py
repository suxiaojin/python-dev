'''
multiprocessing模块
Process类
    (group=None,target=None,name=None,args=(),kwargs={},daemon=None)
    用户组       进程函数      进程名称                      守护进程
返回Process对象

p.name 进程名
p.is_alive() 是否运行
p.start() 创建子进程，并运行进程函数
p.kill() 结束子进程


os.getpid() --获取当前进程 pid
os.getppid() ---获取父进程pid

'''

# import os,time
# def run_proc(*args):
#     print('run_proc Pid=%s' % (os.getpid()))
#     time.sleep(2)
#
# if __name__=='__main__':
#     stime=time.time()
#     for i in range(5):
#         run_proc()
# print('cost time:', time.time()-stime)


'''
互斥锁: from multiprocessing import Lock,semaphore
lock=Lock()  ----创建锁对象
lock.acquire ---获取锁
lock.release() ---释放锁
'''

'''

进程之间资源是不能共享的，进程之间通过消息队列通信

生产者 -------消息队列或数据库 -----消费者

from multiprocessing import Queue
msgq=Queue(size=0)  --创建消息队列
msgq.put ----消息入队
msgq.get ----消息出队
msgq.empty ---消息队列是否为空
msgq.qsize() ----消息队列中消息数量
'''

from multiprocessing import Process,Queue
import os,time
msgq=Queue()

def product(msg):
    #放入消息
    while True:
        msg=input('Entry: ')
        print('product put msg:', msg)
        msgq.put(msg)
        if msg == 'q':
            print('product exit')
            break

def consumer():
    while True:
        msg=msgq.get()
        print('consumer get msg:', msg[::-1])
        if msg == 'q':
            print('consumer exit')
            break

if __name__=='__main__':
    #创建多线程
    p=Process(target=consumer)
    p.start()
    product('this is test')
    p.join()