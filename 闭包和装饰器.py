'''
闭包：函数内部定义函数，内部函数使用外部变量，函数返回值为内部函数
    使用场景：代码复用，装饰器实现
    作用：记忆上一次调用的状态
'''
def cu_pr():
    a=25
    def cc(x):   ##函数内部定义函数
        return a*x*x  ##函数内部使用外部变量
    return cc     ##函数返回值为内部函数
f=cu_pr()



origin=0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos=pos+step
        pos=new_pos
        return pos
    return go
f=factory(origin)   #函数返回值为内部函#数
print(f(2))
print(f(3))
print(f(5))


def genLogFunc(level):
    #level为日志等级
    def logfunc(msg):
        print('{}！msg:{}'.format(level,msg))
    return logfunc

logerr=genLogFunc('error')
logerr('test')
logwar=genLogFunc('waring')
logwar('kkk')


'''
装饰器: 在不修改某个函数情况下，为函数增加新功能
        装饰器返回值为新的函数
        装饰器原理与闭包类似
        decorate 1
        func     3  ----之后被调用的函数,所以需要多少参数，在 wrapper中就传入多少
        wrapper  2 -----  2中调用3，返回2
        f1=decorate(f1)
'''
#装饰器带参数
def decolog(level):
    print('call decolog')
    def deco(func):
        print('call deco')
        def logfunc(msg):
            print('%s:'%level,end='')     #相当于在f1上增加了一个打印的功能
            func(msg)
        return logfunc
    return deco

@decolog('error')
def f1(msg):
    print('%s'%(msg))
f1('this is error')




import time
def decorator(func):
    def wrapper(*args,**kwargs):
        print(time.time())
        func(*args,**kwargs)
    return wrapper      #装饰器返回值为函数

@decorator
def f1(k1):
    print('this is a function '+ k1)

@decorator
def f2(k1,k2):
    print('this is a function '+ k1+k2)

@decorator
def f3(k1,k2,**kwargs):
    print('this is a function '+ k1+k2)
    print(kwargs)

f1('aa')
f2('bb','cc')
f3('e','d',g=1,t=3)

#f=decorator(f1)
#f()