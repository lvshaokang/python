#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
字符串
'''
s = "hello"
'''
#通过脚标获取指定位置元素
print(s[1])
#len()获取字符串长度
print(len(s))
#循环遍历字符串
for i in range(0,len(s)):
	print(s[i])
'''
#脚标越界
# print(s[6])
#从右向左，最右边元素的脚标从-1开始，向右一次减一
# print(s[-1])
# print(s[-2])

#切片
#注意：切片切出来的子字符串是左闭右开的
# line = "zhangsan,20"
# name = line[0:7]
# print(len(line))
# name = line[0:8]
# print(name)
# age = line[9:11]
# print(age)

#切片步长
# s = "abcde"
# print(s[1:])
# print(s[1:-1])
# print(s[1:-2])
#各一个位置取一个元素
# print(s[0::2])
#等价于
print(s[::2])