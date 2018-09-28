#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
异常处理
'''
'''
#捕获多个异常
try:
    print(num)
    open("test.txt","r")
except (NameError,FileNotFoundError) as err:
    print(err)
print("哈哈哈")
'''
'''
# #try{ return } finally 代码块中,先执行finally,然后再计算return(此时返回值已经提前计算好了，若finally中有return,返回值仍然不会改变)
f = None
try:
    print(num)
    f = open("text.txt","r")
    print("嘿嘿嘿")
except NameError as err1:
    print(err1)
except Exception as err2:
    print("捕获到了全部异常：", err2)
finally:
    print("不论什么情况下，都会执行我")
    if f != None:
        print("关闭文件")
        f.close()
# #finally应用场景：常用于关闭文件、数据库连接等，在程序运行过程中无论是否发生异常都要处理

print("哈哈哈")
'''


# 函数嵌套异常传递
def test1():
    print("-----test1-1-----")
    print(num)
    print("-----test1-2------")


def test2():
    print("*******test2-1******")
    try:
        test1()
    except Exception as err:
        print("捕获到了test1函数的异常", err)
    print("*******test2-2******")


test2()
