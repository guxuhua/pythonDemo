# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/22
# description : 文件流的读取和异常处理
#获取文件中的内容
import os
if os.path.exists("test.txt"):
    data = open("test.txt")
    for d in data:
        # 抓取异常
        try:
            (k, v) = d.split(":")
            print k + "的值是:" + v
        except:
            pass
    data.close()
else:
    print 'File Is Not Exit!'
