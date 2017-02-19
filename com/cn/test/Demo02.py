# -*- coding: UTF-8 -*-
# 运行
class Person:
    __name=""
    def __init__(self,name):
        self.__name=name

    def getName(self):
        return self.__name

print ("结束")
p=Person("guxh")
print(p.getName())