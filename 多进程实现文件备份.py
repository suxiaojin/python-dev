import os
import multiprocessing

def copy_file(q,file_name,old_folder_name,new_folder_name):
    old_f=open(old_folder_name+'/'+file_name, 'rb')
    content=old_f.read()
    old_f.close()
    new_f=open(new_folder_name+'/'+file_name,'wb')
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():
    old_folder_name=input('请输入需要备份的文件夹的地址:')
    try:
        new_folder_name=old_folder_name+'_备份'
        os.mkdir(new_folder_name)
    except:
        pass
    file_names=os.listdir(old_folder_name)
    po=multiprocessing.Pool(5)
    q=multiprocessing.Manager().Queue()
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,old_folder_name,new_folder_name))
    po.close()
    all_file_num=len(file_names)
    copy_ok_num=0
    while True:
        file_name=q.get()
        print('\r拷贝的进度: %.2f %%' %((copy_ok_num+1)*100/all_file_num),end='')
        copy_ok_num+=1
        if copy_ok_num >=all_file_num:
            break

if __name__=='__main__':
    main()

'''
v2:实现文件夹与文件的拷贝
'''
import os,filecmp,shutil,sys

def usage():
    print('sourcedir and dstdir must be existing absolute path of certaiin directory')
    sys.exit(0)


def autoBackup(scrDir,dstDir):
    if ((not os.path.isdir(scrDir)) or (not os.path.isdir(dstDir)) or (os.path.abspath(scrDir) != scrDir) or (os.path.abspath(dstDir) != dstDir)):
        usage()

    for item in os.listdir(scrDir):
        scrItem=os.path.join(scrDir,item)
        dstItem=scrItem.replace(scrDir,dstDir)

        if os.path.isdir(scrItem):
            if not os.path.exists(dstItem):
                os.makedirs(dstItem)
                print('make directory' + dstItem)
            autoBackup(scrItem,dstItem)

        elif os.path.isfile(scrItem):
            if ((not os.path.exists(dstItem)) or (not filecmp.cmp(scrItem,dstItem,shallow=True))):
                shutil.copyfile(scrItem,dstItem)
                print('file:' + scrItem + '==>' + dstItem)

def visitDir(path):
    global totalSize
    global fileNum
    global dirNum

    for lists in os.listdir(path):
        sub_path=os.path.join(path,lists)
        https: // blog.csdn.net / Drek_Hu / article / details / 109137247














Spath=input('输入源文件夹路径：')
Dpath=input('输入目标文件夹路径')
autoBackup(Spath,Dpath)

