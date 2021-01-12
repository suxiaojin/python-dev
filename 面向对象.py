"""
类： 具有相同属性与行为的对象的集合体、是一个抽象概念
对象：类的一个实例，具体的存在对象
例子：
     人是一个抽象的概念，一个类，它是所有人的一个抽象
     小明是人类的对象，实际存在的一个实例，有具体的属性和行为

类有2部分组成： 属性与方法
    实例方法： 一个参数必须为self,只能实例自己调用
    静态方法: 用@staticmethod装饰，类可以直接调用
    类方法: 使用@classmethod装饰，类可以直接调用

面向对象： 抽象、继承、封装、多态
super函数用于调用父类方法
    super().func()
对象初始化: __init__方法
私有属性： 以2个下划线开头 __age，这种属性只能通过实例方法进行访问。

    @property,将方法变为属性去访问

self与对象有关，与类无关
self代表的实例，对象、而不是类
self就是实例

"""
#创建类与对象
# class test():
#     pass
# obj=test()

class Persion:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def get_age(self):
        return self.__age
p=Persion('su',33)
print(p.get_age())
