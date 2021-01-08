# import random
# def get_random(a,b):
#     return random.randint(a,b)
#
# def guess(x):
#     while True:
#         n=input('Entry:')
#         if n=='q':
#             print('退出')
#             break
#         n=int(n)
#         if n > x:
#             print('输入过大')
#         elif n < x:
#             print('输入过小')
#         else:
#             print('congra %d' %x)
#             break
# x=get_random(1,20)
# guess(x)
# nums=[1,2,3]
# tmp=str(nums)
# print (tmp)
# tmp=tmp[1:-1]
# tmp=tmp.split(',')
# S=''
# print(S.join(tmp))

##练习  给定两个字符串s1 s2 判断s2是否为s1旋转而成
def is_fliped_str(s1,s2):
    if s1 == s2:
        return True
    len1=len(s1)
    len2=len(s2)
    if len1 != len2:
        return False
    i = 0;
    while i < len1:
        sub1=s1[:i]
        sub2=s1[i:]
        s3=sub2+sub1
        if s2 == s3:
            return True
        i+=1
    return False
s1,s2='abc','cba'
print(s1,s2,is_fliped_str(s1,s2))

def cmpress_str(s):
    if not s:
        return ''
    len1=len(s)
    result=''
    last=s[0]
    n=1
    for val in s[1:]:
        if val == last:
            n+=1
        else:
            result+=last+str(n)

