字符串不能修改
# 1。 查找
find查找字符串位置
#2. 切分
split
    返回切分后子串组成列表
    k='python,c++,java'
    k=k.split(',')
    print(k)


#3. 拼接------join ----将字符串列表转换为字符串
words=['1','2','3']
s=''
print(s.join(words))


#将列表转换为字符串 ---join
nums=[1,2,3]
tmp=str(nums)
print(tmp)
tmp=tmp[1:-1]
print(tmp)
tmp=tmp.split(',')
print(tmp)
s=''
print(s.join(tmp))



#4 访问字符串  [0:4]返回是 0-3的值  左闭右开原则
abcdefg

str[0]
str[1]
str[0:4]  =  abcd

# 5. 替换 ----replace
s='90,None,80,None'
print(s.replace('None','0'))

#None替换为0，只替换1个
print(s.replace('None','0',1))

# 6. strip
strip方法：用于对字符串头尾进行处理
#6. 字符串开头结尾判断
mi=xiaomi
listphone=['xiaomii8s','huaweimeta20','iphone12','xiaomii5x']
for phone in listphone:
    #判断是否以xiaomi开头
    if phone.startswith(mi):
        print(phone)

#7. 字符串格式化
  %d  整数
  %s  字符串

f-string：它会将变量或表达式计算后的值替换进去

>>>name='ruboob'
>>>f'hello {name}'  替换变量
hello ruboob

>>>f'{1+2}'        使用表达式
3

#8 字符串翻转
str='runoob'
print(str[::-1])  ----  boonur


print(''.join(reversed(str)))


#9.format方法  字符串的format方法可以使用{}用来代替%,且参数位置与个数不受限制

#1个占位符，多个参数没问题
f='{} age is '
print(f.format('li',19))
#指定位置{n}对应第n个参数
f='{1} age is {0}'
print(f.format(20,'zhang'))
#指定参数
f='{name} age is {age}'
print(f.format(name='zao',age='20'))



#集合set是一个无序的不重复元素序列
可以使用{}或者set()函数创建集合，注意：创建一个空集合必须使用set()而不是{}.应为{}是用来创建一个空字典
添加元素 s.add(x)   将元素x添加到s集合中，如果已存在，则不进行任何操作
s.pop()
len(s)
s.remove()
s.clear()清空集合

/tmp  /data
/tmp/kk   /data/kk