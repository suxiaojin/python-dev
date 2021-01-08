score=60
if score > 59:
    print('pass')
else:
    print('failed')
print(score)
a=10
b=20
print('a=',a)
i=0
while i<=20:
    print(i,end=',')
    i+=1
'''
break 语句必须与while if  结合使用。跳出当前循环
while 表达式:
    if 表达式1:
        break
'''
# while True:
#     value=input("Entry:")
#     if value=='q':
#         break
#     print(value)

'''
continue 也必须与while for结合使用.结束本次循环
while 表达式:
...
continue
...
'''
s='abc12k45b'
for v in s:
    if v>='1' and v<='9':
        print(v,end='')
        continue
    print('*',end='')


s='ed23n4'
for v in s:
    if v>='1' and v<='9':
        break
    print(v)
help(range)

for i in range(2,21,2):
    print(i,end=' ')

def isodd(a):
    if a%2:
        print("%d is odd" %a)
isodd(10)
isodd(11)