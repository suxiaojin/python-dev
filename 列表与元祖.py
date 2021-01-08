# 1.列表相关函数
# max()   获取最大值
# len()   获取长度
# sum() 求和
#
# l=[1,2,10,4]
# print('len(l)',len(l))
# print('max(l)',max(l))
# print('sum(l)',sum(l))
#
# #列表主要操作：增删改查
# L.append   --在列表尾部添加
# L.insert(index,obj)  --指定索引插入
# L.extend --尾部扩展列表
#
# #列表统计与查找
# L.count
# L.index
#
# #列表删除
# L.pop(index=-1,/) --删除病返回index对应的value,默认值为01
# L.remove(valus,/)  --删除第一次出现的value值，如果不存在，则异常
# L.clear()  -- 清空列表
#
# #元祖相关方法,元祖不可变
# 1.查找元祖：
# T.count(valus) -- 统计value在L中出现的次数
# T.index(value)

# def insert_value(nums):
#     while True:
#         line=input('输入数值：')
#         if line == 'q':
#             break
#         x=int(line)
#         for i,val in enumerate(nums):
#             if val > x:
#                 nums.insert(i,x)
#                 break
#         else:
#                 nums.append(x)
#         print('result:',nums)
# listen=[1,3,6]
# insert_value(listen)


# s='php c pytohn java c++'
# def sort_wds(s):
#     wds=s.split()
#     wds.sort(key=len)
#     return wds
# r=sort_wds(s)
# print(r)

# def del_vals(lums):
#     for val in lums:
#         count=lums.count(val)
#         if count > 1:
#             lums.remove(val)
# lums=[1,2,1,2,2,2]
# print(lums)
# del_vals(lums)

