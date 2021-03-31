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
