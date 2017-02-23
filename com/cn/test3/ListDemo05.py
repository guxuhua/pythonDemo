# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/21
# description : 嵌套的列表数据也做打印

# 初始化列表数据
Movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#直接打印
for d in Movie:
    print d

print "==========This Is Dividing Line=========="
#判断列表元素为列表的
for d in Movie:
    if isinstance(d, list):
        for dd in d:
            print dd
    else:
        print d
