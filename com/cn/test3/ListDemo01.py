# -*- coding:utf-8 -*-
# fileename : ListDemo.py
# description : list demo

##方法用来获取用户输入，动态扩展一个已知的列表
def  __getList__() :
    cast = []
    while True:
        print "please input something: "
        a = raw_input("your input:")
        print a
        if a == 'q':
            break
        cast.append(a)
    print "end input"
    print cast
    return cast

#调用方法__getList__
b=__getList__()
print type(b)