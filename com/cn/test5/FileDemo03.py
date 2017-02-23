# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/22
# description : 通过抓取异常的方式对文件做处理
try:
    data = open("test.txt")
    for d in data:
        try:
            (k,v) = d.split(":")
            print k+"的值是:"+v
        except ValueError:
            print d+"这条记录结构有问题"
except IOError:
    print "文件不存在"
data.close()
print '文件已经关闭'