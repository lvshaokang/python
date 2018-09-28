#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
单例模式
'''


# __new__方法
class DataBaseObj(object):
    def __init__(self):
        print("----init构造方法-------")

    def __new__(cls):  # cls代表的是类对象
        print("cls_id: ", id(cls))
        return object.__new__(cls)  # 返回对象引用


# print("DataBaseObj_id: ",id(DataBaseObj))
# db = DataBaseObj()
# print(db)

'''
实例化对象的过程：
1）调用__new__方法创建对象，并返回创建的对象的引用
2）调用__init__构造方法初始化对象，将先创建的对象的引用作为参数传入，此时self指向的是上一步new方法创建的对象的引用
3）初始化对象结束，将对象的应用返回给db变量
'''


# 单例类、
class SingleObj(object):
    instance = None

    def __init__(self):
        print("---init----")

    def __new__(cls):
        if cls.instance == None:
            cls.instance = object.__new__(cls)  # 类属性指向实例对象
        return cls.instance
        # return object.__new__(cls)


s1 = SingleObj()
print(id(s1))
s2 = SingleObj
print(id(s2))
