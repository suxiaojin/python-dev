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

'''
装饰器: 在不修改某个函数情况下，为函数增加新功能
        装饰器返回值为新的函数
        装饰器原理与闭包类似
'''
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