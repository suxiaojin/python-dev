#os模块
'''
目录操作 --增删改查
    os.listdir ---获取目录下所有文件
    os.mkdir ---创建目录
    os.remove ---删除文件
    os.rmdir ---删除目录
    os.removedirs ---删除目录及目录下所有内容
    os.chdir ---切换到指定路径
    os.rename ---修改文件名称

文件操作：

路径处理
    os.path.exists(path) ---判断path是否存在
    os.path.isdir(path,/) ---判断路径是否是目录
    os.path.isfile(path) ---判断路径

    os.getcwd() ---获取当前路径
    os.path.join() ---路径拼接

系统相关操作
    os.walk ---遍历指定目录及子目录

'''
import os
fpath=r'E:\kkk'
items=os.walk(fpath)
print(next(items))