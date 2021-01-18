'''
pymysql
 连接 -----操作-----提交----关闭
    连接数据库 = db=pymysql.connect(数据库地址,用户名,密码,库名)
    获取游标 = cursor=db.cursor()

    操作: 读： cursor.execute(sql)
              data=cursor.fetchone(),---读取一条    data=cursor.fetchmany(2),--读取2条     data=cursor.fetchall() --读取所有

         写： cursor.execute(sql)      cursor.executemany(sql) 多次插入数据
             db.commit()

    关闭数据库: cursor.close()
              db.close()

'''

vals=[['test3',9007,'hardware_eg',15000,10],['test4',9008,'software_eg',20000,11]]
indata=[]
for item in vals:
    print(item)
    vals=['''%s'''%ele for ele in item]
    print(vals)
    idata=','.join(vals)
    print(idata)
    indata.append("(%s)"%idata)
    print(indata)
