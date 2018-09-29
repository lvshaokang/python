#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# rs = re.match("chinahadoop","baidu.cn")
# print(type(rs))
# if rs != None:
#     print(rs.group())

# 单字符匹配
# .\n之外的单字符
# rs = re.match(".","1")
# print(rs.group())
# rs = re.match(".","a")
# print(rs.group())
# rs = re.match(".","abc")
# print(rs.group())
# rs = re.match("...","abc")
# print(rs.group())
# rs = re.match(".","\n")
# print(type(rs))
# print(rs)

# \s匹配空白字符
# rs = re.match("\s"," ")
# print(type(rs))
# \S匹配非空白字符

# rs = re.match("\S"," ")
# print(type(rs))
# rs = re.match("/S","abc")
# print(type(rs))
# print(rs)

# \w匹配单词字符
# rs = re.match("\w","*")
# print(type(rs))

# [] 匹配[]中列举的字符，字符之间是或的关系
# rs = re.match("[Hh]","Hello")
# if rs != None:
#     print(rs.group())
# rs = re.match("[0123456789]","3")
# if rs != None:
#     print(rs.group())
# 等价简单写法
# rs = re.match("[0-9]","6")
# if rs != None:
#     print(rs.group())

# 数量表示
# *出现任意次 \d 匹配数字
# rs = re.match("1\d*","2345")
# if rs != None:
#     print(rs.group())

# rs = re.match("1\d*","12345abc")
# if rs != None:
#     print(rs.group())

# + 至少出现一次
# rs = re.match("\d+","123abc")
# print(rs)

# ？至多出现一次，0次或者1次
# rs = re.match("\d?","abc")
# print(rs)
#
# rs = re.match("\d?","123abc")
# print(rs)

# {m}出现m次
# rs = re.match("\d{4}","1234abc")
# print(rs)

# {m,} 至少出现m次
# rs = re.match("\d{0,}","12345678abc")   #等价*任意次
# print(rs)

# rs = re.match("\d{1,}","12345678abc")   #等价+
# print(rs)
# rs = re.match("\d{0,1}","abc") #等价？
# print(rs)

# 练习：匹配一个手机号

'''
分析过程：
手机号11位，第一位以1开头，第2位3/5/7/8,第3位到第11位是0-9数字
'''
# rs = re.match("1[3578]\d{9}","13612345678")
# print(rs)
#
# rs = re.match("1[3578]\d{9}","14612345678")
# print(rs)
#
# rs = re.match("1[3578]\d{9}","13612345678abc")
# print(rs)

# 转义字符 \
# str1 = "hello\\world"
# print(str1)
# str2 = "hello\\\\\\world"
# print(str2)
# #原生字符串
# str3 = r"hello\\world"
# print(str3)

# 正则表达式里的转义字符
str3 = r"hello\\world"
# print(str3)
# rs = re.match("\w{5}\\\\\\\\\w{5}",str3)
# print(rs)

# \w{5}\\\\\\\\\w{5} \\\\\\\\->\\\\正则对象
# rs = re.match(r"\w{5}\\\\\w{5}",str3)
# print(rs)

# 边界表示
# 使用结束边界$完善手机号匹配
# rs = re.match("1[3578]\d{9}$","13612345678")
# print(rs)

# 练习：匹配邮箱
# rs = re.match("\w{3,10}@163.com$","hello_123@163.com")
# print(rs)

# rs = re.match("\w{3,10}@163.com$","he@163.com")
# print(rs)

# rs = re.match("\w{3,10}@163.com$","he@163.comhaha")
# print(rs)

# 点在正则中有特殊含义，如果匹配普通点，需要使用转义字符\
# rs = re.match("\w{3,10}@163\.com$","hello_123@163.com")
# print(rs)

# 匹配分组
# 练习：0-100之间的数字
'''
分析过程：
0，1-9,10-99,100
'''
# rs = re.match("[1-9]\d?$|0$|100$","0")
# print(rs)
#
# rs = re.match("[1-9]?\d?$|100$","0")
# print(rs)

# 分组（）
# rs = re.match("\w{3,10}@(163|qq|outloot)\.com$","hello@163.com")
# print(rs)
# rs = re.match("\w{3,10}@(163|qq|outloot)\.com$","1234567@qq.com")
# print(rs)

# \NUM ->\2
'''
html_str = "<head><title>python</head></title>"
rs = re.match(r"<(.+)><(.+)>.+</\2></\1>",html_str)
print(rs)
html_str = "<head><title>python</title></head>"
rs = re.match(r"<(.+)><(.+)>.+</\2></\1>",html_str)
print(rs)
'''

# 分组别名
html_str1 = "<head><title>python</title></head>"
# rs = re.match(r"<(?P<g1>.+)><(?P<g2>.+).+</(?P=g2)></(?P=g1)>",html_str1)
# print(rs)
# search
# rs = re.search("hello","hahah hello python hello world")
# print(rs)

# findall
# rs = re.findall("hello","hahah hello python hello world")
# print(rs)

# finditer
# rs = re.finditer(r"\w{3,20}@(163|qq)\.(com|cn)","hello@163.com")
# print(type(rs))
# for it in rs:
#     print(it.group())

# sub
# str = "java python c cpp java"
# rs = re.sub(r"java","python",str)
# print(rs)

# str = "a,b,c"
# list = str.split(",")
# for ls in list:
#     print(ls)

# 贪婪和非贪婪模式
rs = re.findall("hello\d*?", "hello12345")
print(rs)
