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

'''
shutil文件夹与文件的操作

copyfileobj(fsrc,fdst,lenght=16*1024)  --- 将fsrc文件内容复制至fdst文件，length为fsrc每次读取的长度，用做缓冲区大小
copyfile(src, dst)： 将src文件内容复制至dst文件
'''