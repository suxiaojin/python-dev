#ATM实现
def atm_query(cidinfo):
    '''查询'''
    return cidinfo.get('money',0)

def atm_in(cidinfo):
    '''存钱'''
    money=int(input('输入存入金额:'))
    cidinfo['money'] += money
    print('存款成功，余额为:',cidinfo['money'])

def atm_out(cidinfo):
    '''取款'''
    money=int(input('输入取出金额:'))
    if money > cidinfo.get('money',0):
        print('余额不足!')
    else:
        cidinfo['money'] -= money
        print('取款成功，还剩余:',cidinfo['money'])

def atm_menu():
    '''菜单'''
    menus={
        'C':'查询余额',
        'O':'取钱',
        'I':'存钱',
        'Q':'退出',
    }
    print(menus)
    cmd=input('输入命令:')
    return cmd
exit_code='Q'

def atm_login(usercards):
    max_try=3
    while True:
        cid=input('输入卡号，输入Q退出:')
        if cid==exit_code:
            break
        if cid in usercards:
            break
        print('请输入正确的卡号:')
    while max_try >0:
        cardinfo=usercards.get(cid)
        pwd=input('输入密码:')
        if cardinfo.get('pwd')==pwd:
            return cardinfo
        max_try-=1
        print('密码错误 ，请重新输入，还可以输入%d次'%max_try)

def main():
    cardsinfo={
        '1001':{'cid':'1001','pwd':'123456','money':456789},
        '1002': {'cid': '1002', 'pwd': '123456', 'money': 123},
    }
    cidinfo=atm_login(cardsinfo)
    if not cidinfo:
        print('登录失败,atm退出')
        return

    while True:
        cmd=atm_menu()
        if cmd=='C':
            money=atm_query(cidinfo)
            print('money:',money)
        elif cmd=='I':
            atm_in(cidinfo)
        elif cmd=='O':
            atm_out(cidinfo)
        elif cmd=='Q':
            break

main()
