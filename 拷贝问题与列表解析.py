#拷贝
p1=[[1,2,3],4]
p2=list(p1)
p2[0][0]=0
p2[-1]=-5
print('p1:',p1)
print('p2:',p2)
#深拷贝
#copy:浅拷贝，只对当前对象进行拷贝，没有对子元素进行拷贝
#deepcopy：深拷贝，对象及其子对象
#迭代对象中包含可变对象（列表、字典），推荐使用深拷贝

import copy
p1=[[1,2],4]
p2=copy.copy(p1)
p3=copy.deepcopy(p1)
p1[0][0]=10
p2[1]=-1
p3[0][1]=100
print('p1:',p1)
print('p2:',p2)
print('p3:',p3)


#列表解析
listv=[i*i for i in range(1,10)]
print(listv)
#列表解析添加条件判断
plist=[90,80,70,60,55]
listpass=[v for v in plist if v >60]
print(listpass)