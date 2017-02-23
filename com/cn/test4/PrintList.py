# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/22
# description : 用来打印列表数据
#function : 用来打印列表数据
print '==========Using PrintList.py=========='
def print_list(data):
    '''use for print list'''
    for d in data:
        if (isinstance(d, list)):
            print_list(d)
        else:
            print d

