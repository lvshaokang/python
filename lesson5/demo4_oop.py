#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
面向对象
'''


class Dog:
    def eat(self):
        print("小狗正在啃骨头!")

    def drink(self):
        print("小狗正在喝水!")


# 创建对象
wang_cai = Dog()
wang_cai.eat()
wang_cai.drink()
print("-------------")
afu = Dog()
afu.eat()
afu.drink()
