# -*- coding:utf-8 -*-
#fileName:WhileDemo01.py
#练习while循环的用法

numbers=raw_input('输入几个数组，用都好分割').split(",")
print numbers
x=0
while x<len(numbers):
    print numbers[x]
    x+=1


