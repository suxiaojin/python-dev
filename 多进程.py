'''
multiprocessing模块处理多进程

'''


from multiprocessing import Process
import os

def run_proc(args):
    print('Child Pid=%s name=%s' % (os.getpid(),args))

if __name__=='__main__':
    print('Parent pid %s' % os.getpid())
    p=Process(target=run_proc, args=('test',))
    p.start()
    p.join()

'''
消息队列使用
'''

from multiprocessing import Process,Queue
import os

msgq=Queue()


def product(msg):
    print(f'product {os.getpid()} put msg:{msg}')
    msgq.put(msg)


def consumer():
    print(f'consumer {os.getpid()} wait msg!')
    msg=msgq.get()
    print(f'consumer {os.getpid()} get msg:{msg}')


if __name__=='__main__':
    p=Process(target=consumer)
    p.start()
    product('this is test!')
    p.join()



from multiprocessing import Process, Queue
import os
import time

msgq = Queue()


def product(msg):
    while True:
        msg = input('Enter:')
        print('product put msg:', msg)
        msgq.put(msg)
        if msg == 'q':
            print('product exit')
            break


def consumer():
    while True:
        msg = msgq.get()
        print('consumer get msg:', msg[::-1])
        if msg == 'q':
            print('consumer exit')
            break


if __name__ == '__main__':
    p = Process(target=consumer)
    p.start()
    product('this is test')
    p.join()