# -*- coding:utf-8 -*-
# filename: ForDemo01.py
# 用来练习for循环
'''this is usding as for'''
#range:含前不含尾
for x in range(-4,5,1):
    if x<0:
        print '负数:',x
    elif x==0:
        print '零:',x
    else:
        print '正数:',x

print '执行完毕'