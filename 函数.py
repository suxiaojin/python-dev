'''
函数三要素：
    函数名

    函数参数
        无参函数
        带参数函数
        带默认值参数
        可变长非关键字参数与关键字参数（*args,**kwargs）
            可变长非关键字参数 args 其它不固定的参数放到args中
            可变长关键字参数  **kwargs
    函数返回值
        return 添加返回值

通俗理解：给定一个输入，通过一定的逻辑与算法，得到一个结果

作用域：

内置函数：
    getattr(object,name) ---返回对象属性值
    >>>class A(object):
...     bar = 1
...
>>> a = A()
>>> getattr(a, 'bar')        # 获取属性 bar 值
1

'''
#可变长非关键字参数（*args）
def my_sum(x,y,*args):
    return x+y+sum(args)
print(my_sum(1,2,3,4,2))

#可变长关键字参数(**kwargs)
#使用场景：函数定义时，关键字参数数量不定时 **kwargs
def func(x,y,*args,z=10,**kwargs):
    print(x,y,args,z,kwargs)
func(1,2,4,5,19,z=20)
func(1,2,4,5,19,z=20,t=999)

'''
匿名函数：---没有名称的函数，用于实现简单的功能
    lambda:关键字、参数、表达式
    函数直接调用表达式结果
    
'''
f=lambda r: r*r*3.14
print(f(10))

ispass=lambda value: value>59 and 'pass' or 'failed'
print(ispass(70))
print(ispass(40))
#匿名函数与if...else使用
ispass2=lambda value: 'pass' if value >59 else 'failed'
print(ispass2(99))
print(ispass2(40))

#多个参数匿名函数
f=lambda x,y,*args: x*y+sum(args)
print(f(2,3,4,5,1))

'''
函数式编程: map 、filet、reduce
            reduce:连续计算，连续调用lambda
            filter过滤器，集合过滤
'''
date=map(lambda x: x*x,range(10))
print(list(date))

list_x=[1,2,3,4,5]
r=reduce(lambda x,y: x+y,list_x)
print(r)


'''
递归函数：函数自己调用自己
def func(value)
    if :
        func()
func()
递归函数关键点： 函数自己调用自己
              函数调用结束条件
              不能超过python支持最大层数
'''







