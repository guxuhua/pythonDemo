# -*- coding:utf-8 -*-
#fileName:IfDemo01.py
x=1
if x>=0:
    if x>0:
        print("正数")
    else:
        print("0")
else:
    print("负数")

def func(y):
    '''判断一个数是正数还是负数还是0'''
    if y>=0:
        if y>0:
            return "正数"
        else:
            return "0"
    else:
        return "负数"
print(func.__doc__)
print(func(9))