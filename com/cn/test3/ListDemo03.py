# -*- coding:utf-8 -*-
# author:顾旭华
# date:2017/02/21
# description :对列表数据进行迭代:For循环
#获取一个动态列表数据
#初始化一个列表数据
data = []
while True:
    print '动态获取一个列表数据'
    a = raw_input('列表元素：')
    print '输入的是: '+a
    if a=='q':
        break
    data.append(a)
#得到初始化值
print data
#动态获取
for d in data:
    print d
print '==============我是分割线=================='
#第二种
for i in range(0,len(data)):
    print data[i]
