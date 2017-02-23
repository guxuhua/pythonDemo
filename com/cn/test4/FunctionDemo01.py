# -*- coding:utf-8 -*-
# author : 顾旭华
# date : 2017/02/22
# description : 引入一个模块，用来打印列表数据
# 初始化一个列表数据
Cast = ['Palin','Cleese','Idle','Jones','Gilliam','Chapman']
Movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
# 导入所需模块
from PrintList import print_list
print_list(Cast)
#另一种导入
print '==========This is Split Line=========='
import PrintList as p
p.print_list(Movie)