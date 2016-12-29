# -*- coding:utf-8 -*- 
import MySQLdb
import sys
import string
import random
class Coupon(object):
    def __init__(self,conn):
        self.conn = conn
    
    def coupon_digit(self,digit,num):
        cursor = conn.cursor()
        for i in range(int(num)):
            choicecode = string.ascii_letters + string.digits
            code = [random.choice(choicecode) for s in range(int(digit))]
            code = "".join(code)
            sql = "insert into coupondata(coupon) values(%s)"
            try:
                cursor.execute(sql,[code])
            except Exception as e:
                print "插入验证码失败 " + str(e)
                cursor.close()
#     def coupon_num(self,num):
#         cursor = conn.cursor()
#         sql = "insert into coupondata(code) values(%s)"
#         for i in range(int(num)):
#             try:
#                 cursor.execute(sql,[i])
#             except Exception as e:
#                 print "插入序号失败 " + str(e)
#                 break
        
    def transfer(self,digit,num):
        try:
            self.coupon_digit(digit,num)
#             self.coupon_num(num)
            self.conn.commit()
        except Exception as e:
            print "插入数据失败" + str(e)
            self.conn.commit()
        finally:
            self.conn.rollback()
           
    
if __name__=="__main__":
    conn = MySQLdb.connect(host = "127.0.0.1",
                       port = 3306,
                       user = "root",
                       password = "your passwd",
                       db = "your db",
                       charset = "utf8"
                       )
    digit = sys.argv[1]
    num = sys.argv[2]
    coupondata = Coupon(conn)
    try:
        coupondata.transfer(digit,num)
    except Exception as e:
        print "出现问题" + str(e)
    finally:
        conn.close() 
    
    






