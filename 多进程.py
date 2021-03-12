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