### 题目说明：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import string
import random
# def codenuber(x,y):
# coupon = ""
# for i in range(200):
#     coupon += str(i) + "\n"
#     for count in range(12):
#        coupon += random.choice(string.hexdigits + string.ascii_uppercase)
# print(coupon)


# ！！！！string相关知识储备
# >>> import string
# >>> string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# >>> string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.digits
# '0123456789'
# >>> string.hexdigits
# '0123456789abcdefABCDEF'
# >>> string.letters
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# >>> string.lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# >>> string.uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# >>> string.octdigits
# '01234567'
# >>> string.punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
# >>> string.printable
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
# >>> string.whitespace
# '\t\n\x0b\x0c\r


def coupon_creator(digit):
    coupon = ""
    for word in range(digit):
        coupon += random.choice(string.hexdigits + string.ascii_uppercase)
    return coupon
def two_hundred_coupons(count,digit):
    data = ""
    for x in range(count):
        data += 'coupon no.'+str(x)+'  '+coupon_creator(digit)+'\n'
    return data
# print(two_hundred_coupons(200,12))
coupondata=open('coupondata.txt','w')
coupondata.write(two_hundred_coupons(200,12))
coupondata.close()



# import random, string
###使用匿名函数lambda编写
poolOfChars  = string.ascii_letters + string.digits
random_codes = lambda x, y: ''.join([random.choice(x) for i in range(y)])

print (random_codes(poolOfChars, 15))


