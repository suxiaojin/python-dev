"""
类： 具有相同属性与行为的对象的集合体、是一个抽象概念
对象：类的一个实例，具体的存在对象
例子：
     人是一个抽象的概念，一个类，它是所有人的一个抽象
     小明是人类的对象，实际存在的一个实例，有具体的属性和行为

类有2部分组成： 属性与方法
    实例方法： 一个参数必须为self,只能实例自己调用  self
    静态方法: 用@staticmethod装饰，类可以直接调用
    类方法: 使用@classmethod装饰，类可以直接调用 cls

面向对象： 抽象、继承、封装、多态
super函数用于子类调用父类方法
    super(子类,self).func()
对象初始化: __init__方法
私有属性： 以2个下划线开头 __age，这种属性只能通过实例方法进行访问。

    @property,将方法变为属性去访问

self与对象有关，与类无关
self代表的实例，对象、而不是类
self就是实例
getattr  :返回对象属性值
"""
#创建类与对象
# class test():
#     pass
# obj=test()

# class Persion:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age
# p=Persion('su',33)
# print(p.get_age())

# class EditStr:
#     #读取用户输入字符创
#     def get_str(self):
#         msg=input('输入编辑字符串: ')
#         self.src=msg
#
#     #删除
#     def do_delete(self,char):
#         self.src=self.src.replace(char,'',1)
#
#     #插入
#     def do_insert(self,where,char):
#         index=self.src.rfind(where)
#         if index >=0:
#             self.src=self.src[:index]+char+self.src[index:]
#
#     #替换
#     def do_replace(self,src,dest):
#         self.src=self.src.replace(src,dest)
#
#     #读取命令
#     def run(self):
#         self.get_str()
#         while True:
#             cmdline=input('输入D/I/R/Q:')
#             cmds=cmdline.split()
#             cmd=cmds[0]
#             if cmd=='D':
#                 self.do_delete(cmds[1])
#             elif cmd=='I':
#                 self.do_insert(cmds[1], cmds[2])
#             elif cmd=='R':
#                 self.do_replace(cmds[1], cmds[2])
#             elif cmd=='Q':
#                 break
#             print(self.src)
#
# obj=EditStr()
# obj.run()

func_map={'D':'do_delete','I':'do_insert','R':'do_replace'}
cmd='D'
if cmd in func_map:
    getattr(self,cmd)