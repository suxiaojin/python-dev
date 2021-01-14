# # 1. 字典不同于序列，使用索引访问元素。字典中使用key,访问元素  d[key]
# # d={1:'one',2:'two'}
# # print(d)
# # print('d[1]:',d[1])
#
# #2. 字典遍历
# #获取key
# d={'name':'sun','age':22,'sex':'man'}
# for key in d:
#     print(key)
#
# #获取key与value
# d={'name':'sun','age':22,'sex':'man'}
# for key in d:
#     print(f'{key}:{d[key]}')
#
# #3.字典修改
# 可以修改和添加
# #4.字典中的key必须是唯一的
#
# #字典相关函数
# len --返回字典长度
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
