# # 1. 字典不同于序列，使用索引访问元素。字典中使用key,访问元素  d[key]
字典可变
d={1:'one',2:'two'}
print(d)
print('d[1]:',d[1])

#2. 字典遍历
#获取key
d={'name':'sun','age':22,'sex':'man'}
for key in d:
    print(key)

# #获取key与value
d={'name':'sun','age':22,'sex':'man'}
for key in d:
    print(f'{key}:{d[key]}')

#得到的是元祖（name:sun）,(age:22),(sex:man)
d={'name':'sun','age':22,'sex':'man'}
for k in d.items():
    print(k)

#3.字典修改
   可以修改和添加,在遍历字典的时候不能修改字典size,添加、删除
    通过转换为列表进行操作
def delkey(data)
    for key in list(data.keys())
        if data[key]==0
            data.pop(key)
#4.字典中的key必须是唯一的

# #字典相关函数
# len --返回字典长度 len(dict)  ---返回键的总数
# sum --对字典所有value求和
#
# #字典相关方法
# fromkeys ----根据序列创建字典，默认值none
# dict.get(key,default=None)   返回指定健的值
# setdefault ----如果key存在你，返回key对应的值，否则添加元素 {key:default}
#     d={1:2,3:4}
#     print(d.setdefault(1,'one'))
#     #d没有改变
#     print(d)
#     #增加新元素
#     d.setdefault('one',1)
#     print(d)

# #字典删除方法
pop,删除字典给定key及对应的值，返回值为被删除的值
popitem，返回并删除最后一组元素



d=dict.fromkeys('1234',-1)
print(d)
print('pop(1):',d.pop('1'))
print(d)
print(d.popitem())
print(d)

# #字典更新
d.update()

#统计字符次数
s='aaabbbkkkwttg'
def count_chr(s):
    d={}
    for val in s:
        if val in d:
            d[val]+=1
        else:
            d[val]=1
    return d
r=count_chr(s)
print(r)

#统计字符次数
from collections import Counter
s='xiaomi huawei apple vivo'
c=Counter(s)
print(c)

{i:3,'a':6}




#记录用户名、密码
uinfo={}
def getUserInfo():
    name=input('输入用户名：')
    pwd=input('输入密码:')
    return name,pwd

def addUserInfo(info,name,pwd):
    result=True
    if uinfo.get(name):
        result=False
        print('用户名:%s已经存在'%name)
    else:
        iteam={}
        iteam['name']=name
        iteam['pwd']=pwd
        info[name]=iteam
        print('用户:%s添加成功:%s'%(name,iteam))
    return result

def main():
    while True:
        uname,pwd=getUserInfo()
        ret=addUserInfo(uinfo,uname,pwd)
        msg=input('continue?q:退出,anykey:continue')
        if msg=='q':
            break

main()
for item in uinfo.items():
    print(item)

#统计字数
words='this is a test englisg songs sulter edsondd'
def countchr(data):
    result={}
    for c in data:
        if c in result:
            result[c]+=1
        else:
            result[c]=1
    return result
c=countchr(words*100)
print(c)

#生成学生成绩

import random
#生成字典
def getscores(nums):
    scores={}
    for i in range(1,nums+1):
        item={}
        #添加成绩
        item['math']=random.randint(50,100)
        item['chinese']=random.randint(50,100)
        scores[i]=item
    return scores

#计算每个学生总分
def sumScores(info):
    for key in info:
        #获取元素
        item=result[key]
        vals=list(item.values())
        item['all']=sum(vals)

#找出最高分
def findMax(info):
    #记录最大值
    maxval=-1
    #记录最大值对应的key
    ret=-1
    #遍历字典，获取key与valus
    for key,item in info.items():
        #item为字典，获取总分，若总分大于当前记录值，更新记录
        if item['all'] > maxval:
            ret=key
            maxval=item['all']
    return ret

#遍历列表
def dumpDict(info):
    for item in result.items():
        print(item)

#创建字典
result=getscores(5)
#遍历字典
dumpDict(result)
#使用前面生成的result
sumScores(result)
print('计算总分后:')
dumpDict(result)
name=findMax(result)
print('最高分为：',name)

