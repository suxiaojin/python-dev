'''
多进程处理队列
q.put()       程序中数据放入到队列中
q=multiprocessing.Queue()   #声明队列
multiprocessing.Process(target=xxx,args=(q))    多进程处理队列

multiprocessing模块处理多进程


进程池处理队列

# 创建出进程池   最多5个子进程同时进行
po = multiprocessing.Pool(5)

# 创建一个队列
q = multiprocessing.Manager().Queue()
po.apply_async(xxx,args=(q))

 for file_name in file_names:



'''


from multiprocessing import Process
import os


def run_proc(args):
    print('Child Pid=%s name=%s' % (os.getpid(), args))


if __name__ == '__main__':
    print('Parent pid %s' % os.getpid())
    p=Process(target=run_proc, args=('test',))
    p.start()
    p.join()

'''
进程间通信--消息队列使用 Queue()
'''

from multiprocessing import Process,Queue
import os

msgq=Queue()  #创建队列


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



'''

统计多个目录下的所有文件

'''

import hashlib
import os
import time
from multiprocessing import Pool

fpath='/var/lib/docker'
#统计文件信息

def countfiles(dir,files):
    for file in files:
        fpath=os.path.join(dir,file)
        fsize=os.path.getsize(fpath)
        f=open(fpath,'rb')
        fbuf=f.read()
        md5=hashlib.md5(fbuf)
        md5val=md5.hexdigest()

#遍历目录

def listDir(rootdir):
    iterdir=os.walk(rootdir)
    for rdir,dirs,flist in iterdir:
        #遍历所有文件
        if flist:
            countfiles(rdir,flist)


if __name__ == '__main__':
    fpath = '/var/lib/docker'
    stime=time.time()
    dirs=os.listdir(fpath)
    pools=Pool(processes=3)
    for item in dirs:
        pdir=os.path.join(fpath,item)
        pools.apply_async(listDir, args=(pdir,))
    pools.close()
    pools.join()
    print('run time:', time.time() - stime)





