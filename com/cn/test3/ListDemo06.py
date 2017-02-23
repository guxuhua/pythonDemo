# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/21
# description : 通过函数的形式解决列表数据多层嵌套的问题
# 初始化列表数据
Movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]


#函数打印元素
def print_list(list_data):
    for data in list_data:
        if isinstance(data,list):
            for d in data:
                print d
        else:
            print data

# 对嵌套的列表做处理
for m in Movie:
    if isinstance(m,list):
        print_list(m)
    else:
        print m
