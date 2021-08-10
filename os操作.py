#os模块
'''
目录操作 --增删改查
    os.listdir ---获取当前目录下的文件和文件夹
    os.mkdir ---创建目录
    os.remove ---删除文件
    os.rmdir ---删除目录
    os.removedirs ---删除目录及目录下所有内容
    os.chdir ---切换到指定路径
    os.rename ---修改文件名称
    os.makedirs ---递归创建文件夹     mkdir -p
    os.path.getsize
    os.walk ---- 目录下有文件和文件夹的话。它只会walk文件夹    根目录 （/）  根目录下的文件夹(/tmp)   根目录下的文件(/tmp/kk.py)
                                                        /tmp        /tpm/kk               /tmp/kk/cc.log
                结合for 显示出目录，文件夹、文件

文件操作：

路径处理
    os.path.exists(path) ---判断path是否存在
    os.path.isdir(path,/) ---判断路径是否是目录
    os.path.isfile(path) ---判断是文件

    os.getcwd() ---获取当前路径
    os.path.join() ---路径拼接


'''
import os
fpath=r'E:\kkk'
items=os.walk(fpath)
print(next(items))

'''
filecmp.cmp(f1,f2[,shallow]) ----比较两个文件内容是否匹配。f1,f2,是文件的路径。shallow指定是否考虑本身的属性

filecmp.cmpfiles(dir1,dir2,common[,shallow]) -----比较2个文件夹内指定文件是否相等
'''