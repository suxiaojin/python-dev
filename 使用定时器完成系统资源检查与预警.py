'''
需求：
    1.定时检查系统资源   psutil
    2.系统资源超过预设值，触发报警   APScheduler
    3.对指定用户发送报警

'''

#资源获取 psutil
import psutil
def get_sys_info():
    sysinfo={}
    sysinfo['cpu']=psutil.cpu_percent()
    sysinfo['memory']=psutil.virtual_memory().percent
    sysinfo['disk']=psutil.disk_usage('/').percent
    return sysinfo
sysinfo=get_sys_info()
print(sysinfo)

#读取预警值
'''
ini文件
[level]
    cpu=60
    memory=80
    disk=90
    
[mail]
    sender='xxx@126.com'
    pwd='passwd'
    recver='1234567@qq.com'
'''

#设置预警
from configparser import ConfigParser
path='/home/config/warning.ini'    # --设置预设值[level] cpu=60    memory=60   disk=80

def check_sys(path,sysinfo):
    waring=0
    #创建configparser对象
    config=ConfigParser()
    ##读取ini文件，cpu\mem\disk
    readr=config.read(path)
    sections='level'
    keys=['cpu','memory','disk']
    winfo={}
    for key in keys:
        winfo[key]=config.getfloat(sections,key)
    for key in keys:
        if sysinfo[key] > winfo[key]:
            waring=1
    return waring
check_sys(path,sysinfo)


#邮件发送，读取用户信息，并发送邮件
from configparser import ConfigParser
path='/home/config/warning.ini'

def get_mail_info(path):
    config=ConfigParser()
    reader=config.read(path)
    sections='mail'
    keys=['sender','pwd','receiver']
    mailinfo={}
    for key in keys:
        mailinfo[key]=config.get(sections,key)
    return mailinfo

##发送邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send_mail(sender,passwd,to_addrs,msg,subject):
    message=MIMEText(msg,'plain','utf-8')
    message['Sunject']=Header(subject,'utf-8')
    smtp=smtplib.SMTP()
    smtp.connect('smtp.163.com',25)
    smtp.login(sender,passwd)
    smtp.sendmail(sender,to_addrs,message.as_string())
    smtp.quit()
sender='xxx'
passwd='pwd'
to_addrs=['xxx@qq.com']
msg='info:'
subject='系统资源预警'
send_mail(sender,passwd,to_addrs,msg,subject)

#代码整合
def check_sys_info(path):
    sys_info=get_sys_info()
    if check_sys(path=path,sysinfo=sys_info):
        mail_info=get_mail_info(path)
        msg=''.join([f'{k}:{v},\n' for k,v in sysinfo.items()])
        subject='预警信息'
        send_mail(sender,passwd,to_addrs,msg,subject)
path='/home/config/warning.ini'
check_sys_info(path)


#定时任务
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
if __name__=='__main__':
    scheduler=BlockingScheduler()
    #每隔固定时间执行check_sys_info任务，两分钟检查一次
    scheduler.add_job(check_sys_info,'interval',seconds=120)
    try:
        scheduler.start()
    except
        pass
    
#整理成类，最后代码如下：

import psutil,smtplib
from configparser import ConfigParser
from email.mime.text import MIMEText
from email.header import Header
from apscheduler.schedulers.blocking import BlockingScheduler

class SysWarning:
    def __init__(self,config_path):
        self.inipath=config_path

    def get_sys_info(self):
        sysinfo={}
        sysinfo['cpu']=psutil.cpu_percent()
        sysinfo['memory']=psutil.virtual_memory().percent
        sysinfo['disk']=psutil.disk_usage('/').percent
        return sysinfo

    def check_sys(self,sysinfo):
        warning=0
        config=ConfigParser()
        config.read(self.inipath)
        sections='level'
        keys=['cpu','memory','disk']
        winfo={}
        for key in keys:
            winfo[key]=config.getfloat(sections,key)
        for key in keys:
            if sysinfo[key] > winfo[key]:
                warning=1
        return warning

    def get_mail_info(self):
        config = ConfigParser()
        config.read(self.inipath)
        sections = 'mail'
        keys = ['sender', 'pwd', 'receiver']
        mailinfo = {}
        for key in keys:
            mailinfo[key] = config.get(sections, key)
        return mailinfo

    def send_mail(self,sender, passwd, to_addrs, msg, subject):
        message = MIMEText(msg, 'plain', 'utf-8')
        message['Sunject'] = Header(subject, 'utf-8')
        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com', 25)
        smtp.login(sender, passwd)
        smtp.sendmail(sender, to_addrs, message.as_string())
        smtp.quit()

    def check_sys_info(self):
        sys_info = sys.get_sys_info()
        if check_sys(sys_info):
            mail_info = self.get_mail_info()
            msg = ''.join([f'{k}:{v},\n' for k, v in sys_info.items()])
            subject = '预警信息'
            print('mail_info:',mail_info)
            self.send_mail(mail_info['sender'],mail_info['pwd'],mail_info['receiver'],msg,subject)

if __name__=='__main__':
    path='/home/config/warning.ini'
    scheduler=BlockingScheduler()
    obj=SysWarning(path)
    #每隔固定时间执行check_sys_info任务，两分钟检查一次
    scheduler.add_job(obj.check_sys_info,'interval',seconds=120)
    try:
        scheduler.start()
    except (KeyboardInterrupt,SystemExit):
        pass










