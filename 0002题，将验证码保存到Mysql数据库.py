# -*- coding:utf-8 -*-
import MySQLdb
import random
import string
import sys



def coupondata(s, num):
    cursor = conn.cursor()
    for i in range(num):
        choicecode = string.ascii_letters + string.digits
        code = [random.choice(choicecode) for i in range(int(s))]
        code = "".join(code)
        sql = "insert into test(code) values(%s)"
        try:
            cursor.execute(sql,[code])
        except BaseException as e:
            print(e)
            break
    conn.commit()
    cursor.close()
    conn.close()
    print '完成'


if __name__ == "__main__":
    conn = MySQLdb.connect(host="127.0.0.1",
                           port=3306,
                           user="root",
                           password="cs1030",
                           db="test",
                           charset="utf8"
                           )

    print coupondata(13,200)







