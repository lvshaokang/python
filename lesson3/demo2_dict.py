'''
字典
'''
# user_info_list = ["悟空",100,"male","取经"]
# user_info_list[3] = "取经|偷桃"
# print(user_info_list)
#定义存储个人信息的字典
# user_if_dict = {"name":"悟空","age":100,"gender":"male","job":"取经"}
# #字典通过key获取对应的值
# print("{}的年龄：{}，性别：{}，工作内容：{}".format(user_if_dict["name"],user_if_dict["age"],user_if_dict["gender"],user_if_dict["job"]))
# #字典通过key修改已存在的值
# user_if_dict["job"] = "取经|偷桃"
# print(user_if_dict["job"])
#字典中的key不能重复，如果出现重复key，后边的key会覆盖前边的key
# user_if_dict = {"name":"悟空","age":100,"gender":"male","job":"取经","job":"偷桃","name":"悟空123"}
# print(user_if_dict)

##字典的增删改查
#添加一个键值对
user_info_dict = {"name":"悟空","age":100,"gender":"male","job":"取经"}
# user_info_dict["tel"] = 13812345678
# print(len(user_info_dict))
# print(user_info_dict)
#修改字典中指定键的值
# user_info_dict["tel"] = 13888888888
# print(user_info_dict)

#删除元素
# del user_info_dict["tel"]
# print(user_info_dict)
#删除一个不存在的key将产生异常，报错
# del user_info_dict["tel"]
#查询一个不存在的key，报错
# print(user_info_dict["tel"])
#解决办法
#方法1：
'''
if "tel" in user_info_dict:
	print(user_info_dict["tel"])
else:
	print("tel键不存在")
'''
#方法2：get方法
# print(user_info_dict.get("tel"))
#通过get获取不存在的key，设置默认值
# print(user_info_dict.get("tel","000"))

#使用循环遍历字典
#for循环
#字典内置的keys方法，返回所有的key组成一个序列
# for key in user_info_dict.keys():
#     print("{}:{}".format(key, user_info_dict[key]))

# 字典内置的values方法，返回所有的value组成的一个序列
# for value in user_info_dict.values():
#     print(value)
# items
# for item in user_info_dict.items():
#     print(type(item))
#     print(item)
#     print(item[0])
#     print(item[1])
# for key,value in user_info_dict.items():
#     print("{}:{}".format(key, value))

#clear()清空字典
user_info_dict.clear()
print(user_info_dict)