# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/22
# description : 读取文件内容
import os
print os.getcwd()
#打开文件
data = open('python.txt')
#print data.readline()
for each_line in data:
    print each_line
    (role,saying) = each_line.split(":")
    print role
    print " said:"
    print saying
#关闭文件
data.close()