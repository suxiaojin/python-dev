#文件打开open
fpath= 'E:\\test.txt'
wds='kkk'
f=open(fpath,'w')
f.write(wds)
print(f)
f.close()

#文件写入 w

#文件读写方式 for 循环
fpath= 'E:\\test.txt'
f=open(fpath)
for line in f:
    print(line,end='')
f.close()

#seek操作
