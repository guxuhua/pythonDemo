# -*- coding:utf-8 -*-
#fileName:HelloWorldDemo01.py
class Hello:
    '''This is the Class Called Hello z doc'''
    def fun(self):
        '''This is the function fun z doc'''
        return "Hello World"

print(Hello.__doc__)
print(Hello.fun.__doc__)
