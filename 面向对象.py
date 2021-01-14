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

# func_map={'D':'do_delete','I':'do_insert','R':'do_replace'}
# cmd='D'
# if cmd in func_map:
#     getattr(self,cmd)
import time

class OneEvent:
    def __init__(self,when,where,what):
        self.__when=when
        self.__what=what
        self.__where=where
    @property
    def when(self):
        return self.__when
    @when.setter
    def when(self,when):
        self.__when=when

    @property
    def where(self):
        return self.__where
    @where.setter
    def where(self,where):
        self.__where=where

    @property
    def what(self):
        return self.__what
    @what.setter
    def what(self, what):
        self.__what = what

    def __str__(self):
        return f'时间:{self.when},地点:{self.where},事件:{self.what}'

if __name__ == '__main__':
        cur_time=time.localtime()
        ts=time.strftime('%Y-%m-%d %H:%M:%S',cur_time)
        what="工作"
        where="单位"
        event=OneEvent(ts,where,what)
        print(event)
        print(event.when,event.what,event.where)
        event.when='2020-10-17'
        event.where='公园'
        event.what='休息'
        print(event.when,event.where,event.what)

class EventNote:
    def __init__(self,*args,**kwargs):
        self.events={}
        self.event_id=1

    def add_event(self):
        when=input('输入时间:')
        where=input('输入地点:')
        what=input('输入事件:')
        event=OneEvent(when,where,what)
        self.events[self.event_id]=event
        self.event_id+=1

    def del_event(self):
        try:
            eid=int(input('输入删除ID'))
            event=self.events.pop(eid)
            print('del event:',event)
        except Exception as e:
            print('Error id:',e)

    def find_event(self):
        try:
            eid=int(input('输入查找ID:'))
            event=self.events.get(eid)
            if not event:
                print('no event id')
            else:
                print('find Event:',event)
            return event
        except Exception as e:
            print('Error id:',e)

    def modify_event(self):
        pass


    def dump_events(self):
        if self.events:
            for eid,event in self.events.items():
                print(eid,event)
            print()
        else:
            print('no events')

    def menu(self):
        m={'A':'添加事件','F':'查找事件','D':'删除事件','M':'修改事件','Q':'退出','S':'显示所有事件'}
        print('....................')
        for k, v in m.items():
            print(f'{k}:{v}')

    def run(self):
        func_map={'A':'add_event','F':'find_event','D':'del_event','M':'modify_event','S':'dump_events'}
        while True:
            self.menu()
            cmdline=input('输入：A/F/D/M/Q/S:')
            cmds=cmdline.split()
            cmd=cmds[0]
            if cmd=='Q':
                print('Exit')
                break
            if cmd in func_map:
                func=getattr(self,func_map[cmd])
                func()
enote=EventNote()
enote.run()

