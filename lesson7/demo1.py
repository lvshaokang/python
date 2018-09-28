#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
类属性
'''


class Person:
    # 类属性
    sum_num = 0  # 人类总数

    def __init__(self, new_name):
        self.name = new_name
        # self.sum_num = num
        # Person.sum_num += 1

    # 类方法
    @classmethod
    def add_sum_num(cls):
        cls.sum_num += 1
        print(cls.sum_num)


# 类名调用类方法
Person.add_sum_num()

p1 = Person("zhangsan")
p1.add_sum_num()  # 通过实例对象调用类方法
# 建议：通过类名.类属性方式获取类属性值
# print(Person.sum_num,p1.sum_num)
# p2 = Person("lisi")
# p1.sum_num = 100 #通过实例对象不能够修改类属性值，动态添加实例属性
# print(Person.sum_num,p1.sum_num,p2.sum_num)

# 类方法与实例方法的区别
'''
实例方法->实例对象 :操作实例属性
类方法->类对象 :操作类属性
'''
