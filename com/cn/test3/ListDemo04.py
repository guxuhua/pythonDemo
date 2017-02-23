# -*- coding:utf-8 -*-
# author:顾旭华
# date:2017/02/21
# description :对列表数据进行迭代:While循环

#先动态获取一个列表
data = []
while True:
    print 'Please Input data'
    a = raw_input('input data:')
    print 'a:'+a
    if a == 'q':
        break
    data.append(a)
print data

#while循环迭代列表数据
count = 0
while count<len(data):
    print data[count]
    count+=1

