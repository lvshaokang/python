#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
列表
'''
# name_list = ["zhangsan","lisi","wangwu"]
# print(name_list)
# #通过脚标获取列表元素
# print(name_list[0])

# info_list = ["zhangsan",20,180.5,80,True]
# print(info_list)
#IndexError: list index out of range,脚标越界
# print(info_list[6])
#通过脚标修改元素值
# info_list[3] = 70
# print(info_list)
#while循环遍历列表
'''
list_len = len(info_list)
i = 0
while i < list_len:
	print(info_list[i])
	i += 1
'''
#for循环遍历列表
'''
list_len = len(info_list)
for i in range(0,list_len):
	print(info_list[i])
'''
#append向列表末尾添加元素
# info_lists.append(["xiaobai",25])
# print(info_lists)
#insert(index,item)指定位置添加元素
# info_lists.insert(1,["wangmazi",24])
# print(info_lists)

# 将两个列表元素组合生成一个新的列表
name_list1 = ["唐僧","悟空","八戒"]
name_list2 = ["沙僧","白龙马"]
new_list = name_list1 + name_list2
# print(name_list2)
# print(name_list1)
# print(new_list)

#extend
# name_list1.extend(name_list2)
# print(name_list1)
# print(name_list2)

#删除
# del new_list[1]
# print(new_list)
# new_list.remove("悟空")
# print(new_list)
#pop()默认是删除列表最后一个元素
# new_list.pop()
# print(new_list)
#pop(index)指定删除某个脚标元素
# new_list.pop(1)
# print(new_list)

#切片
group = ["唐僧","悟空","八戒","沙僧","白龙马","唐僧"]
# print(group[1:])
# print(group[1::2])

#in/not int
'''
if "白骨精" in group:
	print("猴哥快来！")
	if "悟空" not in group:
		print("师傅快跑！")
	else:
		print("老孙来也，妖怪哪里跑！")
'''

#sort()
# num_list=[6,3,12,1]
# num_list.sort() #默认升序排列
# num_list.sort(reverse=True) #倒序排列
# print(num_list)

#reverse()列表元素翻转
group.reverse()
print(group)
#count(item)
print(group.count("唐僧"))

