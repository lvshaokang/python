#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
文件操作
'''
import os
import shutil

# f = open("test.txt","r")
'''
f = open("test.txt","w",encoding="utf-8")
f.write("你好")
f.close()

f = open("d://filetest.txt","w",encoding="utf-8")
f.write("hello pythpon")
f.close()

f = open("d://filetest.txt","a",encoding="utf-8")
f.write("\nxxxxxx")
f.close()
'''
# 读数据
'''
f = open("test.txt","r",encoding="utf-8")
data = f.read()
print(data)
f.close()
'''

# readlines()
'''
f = open("test.txt","r",encoding="utf-8")
data = f.readlines()
print(data)
for line in data:
    print("--->{}".format(line),end="")
f.close()
'''
# readline
'''
f = open("test.txt","r",encoding="utf-8")
line = f.readline()
print(line)
line1 = f.readline()
print(line1)
f.close()
'''
# f = open("test.txt","w",encoding="utf-8")
# f.writelines(["zhangsan\n","lisi\n","wangwu\n"])
# f.close()

# with open("test.txt","w",encoding="utf-8") as f:
#     f.writelines(["zhangsan\n","lisi\n","wangwu\n"])

# 创建文件夹
# os.mkdir("D://lamp/SourceCode/bigdata/test/python/lesson5/dir")
# f = open("D://lamp/SourceCode/bigdata/test/python/lesson5/dir/test.txt","w",encoding="utf-8")
# f.close()

# 获取程序运行的当前目录
# path = os.getcwd()
# print(path)

# 获取指定目录下的所有文件
# files = os.listdir("d://")
# print(files)

# 删除空文件夹
# os.rmdir("d://testdir")
# 删除非空文件夹
# shutil.rmtree("D://lamp/SourceCode/bigdata/test/python/lesson5/dir")
