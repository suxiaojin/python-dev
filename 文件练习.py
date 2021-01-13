from functools import reduce
r=reduce(lambda x,y: x+y,range(100))
print(r)

import random
def genscore(fname,nums):
    f=open(fname,'w')
    for i in range(1,nums+1):
        line='{} {}\n'.format(i,random.randint(30,100))
        f.write(line)
    f.close()
genscore('./history.txt',20)
genscore('./chinese.txt',20)

def mergeScore(fname,source1,source2):
    f=open(fname,'w')
    fchinese=open(source1)
    fmath=open(source2)
    chinese_lines=fchinese.readlines()
    math_lines=fmath.readlines()
    for i in range(len(chinese_lines)):
        cline=chinese_lines[i].split()
        mline=math_lines[i].split()
        cline.append(mline[1])
        wline=' '.join(cline)+'\n'
        f.write(wline)
    f.close()
mergeScore('result.txt','./chinese.txt','./math.txt')


# fchinese=open('./chinese.txt')
# chinese_lines=fchinese.readlines()
# print(chinese_lines)
#
# for i in range(len(chinese_lines)):
#     cline = chinese_lines[i].split()
#     print(cline)

def mergeMoreScore(output,nums,*subjects):
    list_subject=[]
    fw=open(output,'w')
    for fname in subjects:
        f=open(fname)
        info=[]
        for line in f:
            info.append(line.split())
        dinfo=dict(info)
        list_subject.append(dinfo)
        f.close()
    for i in range(1,nums+1):
        line=[]
        line.append(str(i))
        for data in list_subject:
            line.append(str(data.get(str(i),0)))
        wline=' '.join(line) + '\n'
        fw.write(wline)
    fw.close()
mergeMoreScore('mresource.txt',20,'./chinese.txt','./math.txt','./history.txt')


f=open('./history.txt')
info=[]
for line in f:
    print(line)
    info.append(line.split())
print(info)
dinfo=dict(info)
print(dinfo)
list_subject=[]
list_subject.append(dinfo)
print(list_subject)
for data in list_subject:
    print(data)
    print(data.get('2'))




