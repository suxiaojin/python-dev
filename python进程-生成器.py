
'''
可迭代对象(iterable)： 能够被 for in 循环的 就叫  比如 列表、元祖、集合、字符串

迭代器（iterator）： 对象(class)。可迭代

需求：循环打印出 书名
    class Bookcollection():
        def __init__(self):
            self.data=['《往事》'，'《只能》'，'《回味》']
        def __iter__(self)
            pass
        def __next__(self)

    books=Bookcollection()
    for book in books:
        print(book)
    一个类中满足上述2中函数，那么它就是迭代器。可以 for in 循环遍历

迭代器---  一次性
'''


class Bookcollection():
    def __init__(self):
        self.data = ['《往事》','《只能》','《回味》']
        self.cur=0

    def __iter__(self):
         return self

    def __next__(self):
        if self.cur>len(self.data):
            raise StopIteration()
        r=self.data[self.cur]
        self.cur+=1
        return r

books = Bookcollection()
print(next(books))
for book in books:
    print(book)


'''
生成器：针对函数来说的
yield:记录上下文，返回一个对象，停止当前运行

'''
def gen(max):
    n=0
    while n<max:
        n+=1
        yield n
g=gen(10000)
print(next(g))     # 出现的是1
print(next(g))     # 出现的是2

for i in g:
    print(i)     # 打印的是1.。。10000
















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