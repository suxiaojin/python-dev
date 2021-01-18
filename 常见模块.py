'''
import pexpect
pexpect.spawn() ---参数
    command ---交互命令
    args ---命令参数
    maxread ---读取缓存大小
    logfile ---指定log 文件
'''

#查看指定目录下的所有文件
args=['ls','-l','/home/data']
c=pexpect.spawd(''.join(args),logfile=sys.stdout)

#连接断开
c.expect(pexpect.EOF)

#连接超时
pexpect.TIMEOUT

#发送命令不加回车
c.send(s)
 #发送命令加回车
 c.sendline(s='')


 #远程登录代码
import pexpect
import sys
#准备账号
server_name='192.168.110.10'
uname='root'
pwd='IexrduZ*!W4pay'
#linux提示符#
prompt='#'
cmd='ssh %s@%s' %(uname,server_name)
c=pexpect.spawn(cmd, logfile=sys.stdout)
#匹配出现提示输入密码:password
c.expect('password')
#发送密码
c.sendline(pwd)
c.expect(prompt)

'''
需求:
本地文件拷贝到远程服务器同一目录
ssh登录远程服务器
计算md5值，并与本地文件比较
'''
import hashlib
import pexpect
import os,sys
class RemoteCopy:
    #初始化,remoteinfo为多个服务器信息列表
    #服务器信息主要包括：用户名、密码、地址、路径
    def __init__(self,remoteinfos,rprompts,lprompts):
        self.remotes=remoteinfos
        self.rprompts=rprompts
        self.lprompts=lprompts

    def getRemoteInfo(self,remote):
        return remote.get('uname'),remote.get('upwd'),remote.get('address'),remote.get('path')

    #拷贝文件到远程服务器
    def scpToRemote(self,listfile):
        files=''.join(listfile)
        for remote in self.remotes:
            uname,upwd,address,remotepath=self.getRemoteInfo(remote)
            print('[%s][%s][%s]'%(uname,upwd,address))
            cmd='scp %s %s@%s:%s' %(files,uname,address,remotepath)
            print(cmd)
            c=pexpect.spawn(cmd)
            self.scpobj=c
            c.expect('password')
            c.sendline(upwd)
            c.expect(self.lprompts)
            print(c.before)
            c.sendeof()

    def checkResult(self,rinfo,linfo):
        listfails=[]
        [listfails.append(key) for key in linfo if rinfo.get(key)!=linfo.get(key)]
        return listfails

    #ssh登录
    def sshLogin(self,remoteinifo):
        uname,upwd,address,path=self.getRemoteInfo(remoteinifo)
        cmd='ssh %s@%s' %(uname,address)
        c=pexpect.spawn(cmd)
        self.c=c
        c.expect('password')
        c.sendline(upwd)
        c.expect(self.rprompts)

    def countRemoteMd5(self,remotepath,files):
        c=self.c
        c.sendline('cd %s'%remotepath)
        c.expect(self.rprompts)
        result={}
        for name in files:
            fname=os.path.basename(name)
            c.sendline('md5sum %s'%fname)
            c.expect(self.rprompts)
            print(c.before)
            lines=c.before.decode('utf-8').split('\r\n')
            md5=''
            for line in lines:
                if fname in line:
                    md5,name=line.split(maxsplit=1)
                    md5=md5.strip()
                    if len(md5)==32:
                        result[fname]=md5
                        break
        return result

    def countLocalMd5(self,flist):
        result={}
        for fpath in flist:
            fname=os.path.basename(fpath)
            f=open(fpath,'rb')
            buf=f.read()
            obj=hashlib.md5(buf)
            result[fname]=obj.hexdigest()
        return result

    def start(self,listfiles):
        self.scpToRemote(listfiles)
        for remote in self.remotes:
            self.sshLogin(remote)
            remote_md5s=self.countRemoteMd5(remote.get(path),.listfiles)
            local_md5s=self.countLocalMd5(listfiles)
            result=self.checkResult(remote_md5s,local_md5s)
            #输出拷贝失败文件
            print('scp to %s path:%s failes:%s'%(remote.get('address'),remote.get('path'),result))

if __name__=='__main__':
    rinfo=[{'uname':'root','upwd':'abc123','address':'19.168.1.1','path':'/root/test'},
           {'uname':'root','upwd':'abc345','address':'19.168.1.2','path':'/root/test1'}]
    rprompts=['#']
    lprompts=['$']
    files=['/home/linux/data/iphone.csv','/home/linux/data/medi.csv']
    remotepath='/root/test'
    handler=RemoteCopy(rinfo,rprompts,lprompts)
    handler.start(files)