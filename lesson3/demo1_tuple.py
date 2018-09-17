'''
元组
'''
# 定义元组，存储数据库信息
db_info = ("192.168.1.1", 3306, "root", "123456")
# 通过脚标查询元组中的元素
# ip = db_info[0]
# port = db_info[1]
# print("ip:{},port:{}".format(ip,port))
# 通过脚标修改元组指定元素的值,错误的做法
# db_info[1] = 8080
# print(db_info)
# del删除元组指定元素,错误做法
# del db_info[1]
# 只包含一个元素的元组,注意元素最后的逗号
# one_tuple = (123,)
# print(one_tuple)
# print(type(one_tuple))
# 错误的定义只包含一个元素的元组，少了元素后的逗号
# one_tuple = (123)
# print(type(one_tuple))
# 空元组
# none_tuple = ()

# 循环遍历元组
# for循环
# for item in db_info:
#     print(item)
# while循环
# i = 0
# while i < len(db_info):
#     print(db_info[i])
#     i += 1
