#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
变量
input输入
print输出
类型转换
'''
#变量的定义
name = "zhangsan" #名字
high = 180 #身高
age = 20 #年龄
weight = 80 #体重

# print(name)
# print(high)
# print(age)
# print(weight)
#变量赋值
# print("---------------------")
# weight = weight + 20
# weight = 100
# print(weight)

#查看变量类型
# print(type(name))
# print(type(age))
'''
name = input("请输入用户名：")
password = input("请输入密码：")
print(type(name))
print(type(password))
'''
#直接输出内容
# print("直接输出内容")
# print('直接输出内容')
#输出变量的值
# name = "zhangsan"
# age = 20
# high = 180.35 #身高，浮点数
# print(name,age)
#格式化换行输出
# print("你的名字是：%s"%name)
# print("你的年龄是：%d"%age)
#格式化无换行输出
# print("你的名字是：%s"%name,end="")
# print("你的年龄是：%d"%age)
#输出的字符串中间换行
# print("中国\n北京")

#浮点数精度表示：%.精度值f
# print("姓名：%s,age：%d,身高：%.2f"%(name,age,high))
# p = 99.99
#在格式化输出的时候%是特殊字符，表示转换说明符，如果想打印普通的%，那么要使用%%表示
# print("你战胜了全国%.2f%%的用户"%p)
#format格式化字符串
# name = "zhangsan"
# age = 20
# high = 180.35 #身高，浮点数
# print("姓名：{}，年龄：{}，身高：{}".format(name,age,high))

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# print("name:%s,age:%d"%(name,int(age)))
#常用的数据类型转换
# a = int("123") #字符串转整型
# print(type(a))
# a = int(3.14)
# print(type(a))
# f = float(3)
# print(type(f))
# f = float("3.14")
# print(type(f))

name = "zhangsan"
Name = "lisi"
print(name)
print(Name)






