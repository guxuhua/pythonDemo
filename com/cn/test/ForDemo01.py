# -*- coding:utf-8 -*-
#fileName:ForDemo01.py
#计算1-100的和
def countSum(x):
    print("开始计算")
    sum = 0
    for i in range(1, x):
        sum = sum + i
    return sum
print (countSum(100))
