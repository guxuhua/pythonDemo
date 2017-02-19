# -*- coding:utf-8 -*-
# fileName:ifDemo01.py
# 练习if用法

'''this if used for test if using'''
def func1(x):
    '''this is the first function'''
    print 'this is the first function'
    if x>1:
        print '大于1'
    elif x==1:
        print '等于1'
    else:
        print '小于1'


x=int(raw_input('please input a number:'))
func1(x)


