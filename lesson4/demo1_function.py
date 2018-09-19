#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
函数
'''
##局部变量和全局变量
# 局部变量

# 设置姓名
'''
def set_name():
    #局部变量
    name = "lijing"
    print(name)
'''

# 获取姓名
'''
def get_name():
    name = "lisi"
    print(name)

set_name()
get_name()
'''

# 全局变量
'''
g_name = "lijing"
def get_name1():
    print(g_name)

def get_name2():
    print(g_name)

get_name1()
print("--------")
get_name2()
'''
# 修改全局变量
'''
g_age = 20
def change_age():
    # 通过在函数内直接修改全局变量的方式是错误的，相当于在函数体内定义了一个与全局变量同名的局部变量
    # g_age = 25
    # print("函数内: ",g_age)
    # 在函数体内通过global声明g_age是全局变量
    global g_age
    print("修改之前:",g_age)
    g_age = 25
    print("修改之后: ",g_age)

change_age()
print("---------------")
print(g_age)
'''
# 全局变量定义的位置
'''
g_num1 = 100
g_num2 = 200
g_num3 = 300
def pring_global_num():
    print("g_num1:{}".format(g_num1))
    print("g_num2:{}".format(g_num2))
    print("g_num3:{}".format(g_num3))
pring_global_num()
'''
# 字典、列表作为全局变量使用，在函数体内修改其中其中的元素值，可以不适用global关键字声明
'''
g_num_list = [1,2,3]
g_info_dict = {"name":"lijing","age":20}

def update_info():
    g_num_list.append(4)
    g_info_dict["gender"] = "male"

def get_info():
    for num in g_num_list:
        print(num)
    for key,value in g_info_dict.items():
        print("{}:{}".format(key,value))
update_info()
get_info()
'''

# 缺省参数
'''
def x_y_sum(x,y=20):
    rs = x + y
    print("计算结果: {}".format(rs))

x_y_sum(10,30)
x_y_sum(10)
'''
# 命名参数
'''
def x_y_sum1(x=10,y=20):
    print(x)
    print(y)
    rs = x+y
    print("计算结果:{}".format(rs))
x_y_sum1(y=40,x=15)
'''
# 不定长参数
'''
def any_num_sum(x,y=10,*args):
    print("args:{}".format(args))
    rs = x+y
    if len(args) > 0:
        for arg in args:
            rs += arg
    print("计算结果：{}".format(rs))

any_num_sum(20)
any_num_sum(20,30)
any_num_sum(20,30,40,50,60,70)
'''
'''
def social_comp(basic_money,**proportion):
    print("缴费基数：{}".format(basic_money))
    print("缴费比例：{}".format(proportion))

social_comp(8000,e=0.2,m=0.1,a=0.12)
'''
# 拆包
'''
def salary_comp(basic_money,*other_money,**proportion):
    print("基本工资：{}".format(basic_money))
    print("其他福利：{}".format(other_money))
    print("缴费比例：{}".format(proportion))
other_money = (500,200,100,1000)
proportion_dict = {"e":0.2,"m":0.3,"a":0.12}

salary_comp(8000,*other_money,**proportion_dict)
salary_comp(8000,other_money,proportion_dict)
'''

# 递归函数
'''
1！ = 1
2!=2 * (2-1)
3! = 3 * 2! 
4! = 4 * 3!  等价于 4 * 3 * 2 * 1
5! = 5 * 4!  等价于 5 * 4 * 3 * 2 * 1
'''
# 计算阶乘
# def recursive_for(num):
#     rs = num
#     for i in range(1,num):
#         rs *= i
#     return rs
# print(recursive_for(4))
'''
def recursive(num):
    if num > 1:
        return num * recursive(num - 1)
    else:
        return num
print(recursive(4))
'''

# 匿名函数
# sum = lambda x,y:x+y
# print(sum(10,40))

# 应用场景
# 1.作为函数的参数
'''
def x_y_comp(x,y,func):
    rs = func(x,y)
    print("计算结果：{}".format(rs))

# x_y_comp(3,5,lambda x,y:x+y)
x_y_comp(3,5,lambda x,y:x*y)
'''
# 2.内置函数参数
'''
user_info = [{"name":"zhangsan","age":20},{"name":"lisi","age":15},{"name":"wangwu","age":30}]
print(user_info)
#升序
user_info.sort(key=lambda info:info["age"])
print(user_info)
user_info.sort(key=lambda info:info["age"],reverse=True)
print(user_info)
'''
