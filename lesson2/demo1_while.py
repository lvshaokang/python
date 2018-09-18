#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
while循环
'''
# 打印数字1到10
# num = 1
# print(num)
# num += 1
# print(num)
#
# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# 打印正三角形
# 每行*号个数=2*行数-1
# 每行左侧的空格数=行数-行号
'''
'''
i = 1 #行号
n = 6 #正三角形打印的行数
while i <= n:
	print(" " * (n-i),end="") #无换行输出，打印每行左侧空格
	j = 1 #控制星号个数
	#打印星号
	while j <= 2*i -1:
		print("*",end="")
		j += 1
	print("")#打印一行换行
	i += 1


# break跳出它所在的整个循环
# 打印1到20的偶数
'''
i = 1
while i <= 20:
	if i % 2 == 0:
		#如果这个偶数能够被10整除，则跳出循环
		if i % 10 == 0:
			break
		print(i)
	i += 1

print("***********************")
'''
# while循环嵌套，break跳出内层循环
# 打印1到4 四个数字，每个数字的上一行都打印与数字相同个数的星号
'''
i = 1
while i < 5:
	j = 0
	while j < i:
		if j == 3:
			break
		print("*",end="")
		j += 1
	print("")
	print(i)
	i += 1
'''
#continue跳出本次while循环
# i = 1
# while i <= 20:
# 	i += 1
# 	if i % 2 == 0:
# 		if i % 10 == 0:
# 			continue
# 		print(i)
#
# print("+++++++++++++++++")