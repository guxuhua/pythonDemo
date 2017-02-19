# -*- coding:utf-8 -*-
# fileName:VarDemo01.py
#在文件开头定义全局变量
print("开始定义全局变量")
_a=1
_b=2

##加法
def fun():
    '''这是一个加法算术方法'''
    print("》》》》加法《《《《")
    #print ("a=",_a)
    #print ("b=",_b)
    #global _a
    _a=3
    return "_a+_b=",(_a+_b)

##减法
def fun1():
    '''这是一个减法算数方法'''
    print("》》》》减法《《《《")
    #print ("a=", _a)
    #print ("b=", _b)
    #global _b
    _b=4
    return "_a-_b=",(_a-_b)

##调用方法
print (fun().__doc__)
print (fun())
print(fun1().__doc__)
print (fun1())

