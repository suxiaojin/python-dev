# 1。 查找
find查找字符串位置
#2. 切分
split
#3. 拼接------join
words=['c++','python','java']
s='/'
print(s.join(words))

nums=[1,2,3]
tmp=str(nums)
print(tmp)
tmp=tmp[1:-1]
tmp=tmp.split(',')
s=''
print(s.join(tmp))

# 4. 替换 ----replace
s='90,None,80,None'
print(s.replace('None','0'))
#None替换为0，只替换1个
print(s.replace('None','0',1))

# 5. strip
strip方法：用于对字符串头尾进行处理
#6. 字符串开头结尾判断
mi=xiaomi
listphone=['xiaomii8s','huaweimeta20','iphone12','xiaomii5x']
for phone in listphone:
    #判断是否以xiaomi开头
    if phone.startswith(mi):
        print(phone)

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