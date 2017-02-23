# -*- coding:utf-8 -*-
# author:顾旭华
# date:2017/02/21
# description :向已知列表中指定位置插入数据
#已知列表
Movie = ['The Hony Grail','The Life Of Brain','The Meaning of Life']
# 插入数据成为：Movie = ['The Hony Grail',1975，'The Life Of Brain',1979，'The Meaning of Life'，1983]
#第一种方法，直接insert方法
def funcOne():
    Movie.insert(1,1975)
    Movie.insert(3, 1979)
    Movie.insert(5, 1983)
    print Movie
    print 'End Function1'

#第二种方法：两个列表整合
def funcTwo():
    #表示年份的列表数据
    Year = [1975,1979,1983]
    print Year
    #整合的新列表数据
    data = []
    for i in(range(0,len(Movie)+len(Year))):
        print i
        if(i%2==0):
            data[i] = Movie[i/2]
        else:
            data[i] = Year[i/2]
    print data
    print 'End Function Two'

#执行方法1
funcOne()
#执行方法2
#funcTwo()