'''
集合set
'''
#集合的定义，元素去重
# student_set = {"zhangsan","lisi","wangwu","zhangsan"}
# print(student_set)
# print(len(student_set))
#set(序列)
#对列表元素去重，并创建一个新的集合
# id_list = ["id1","id2","id3","id1","id2"]
# new_set = set(id_list)
# print(id_list)
# print(new_set)
#对元组中的元素去重，并创建一个新的集合
# id_tuple = ("id1","id2","id3","id1","id2")
# new_set = set(id_tuple)
# print(new_set)
#注意：如果把字符串作为参数传入set函数，则会把每个字符作为个体添加到集合，并且对字符去重
# string_set = set("hello")
# print(string_set)
#创建空集合
# none_set = set()
# print(none_set)
# 注意：创建空字典{}
# none_dict={}
# print(none_dict)
#in 或者not in
# id_list = ["id2","id3"]
# new_set = set(id_list)
# user_id = "id1"
# if user_id in new_set:
#     print("{}存在".format(user_id))
# elif user_id not in new_set:
#     print("{}不存在".format(user_id))
# add(元素)
# new_set.add("id1")
# print(new_set)
#update(序列)
# name_set = {"zhangsan","lisi"}
#添加列表元素到集合
# name_set.update(["悟空","八戒"])
# print(name_set)
#添加元组元素到集合
# name_set.update(("悟空","八戒"))
# print(name_set)
#添加多个序列元素到集合
# name_set.update(["悟空","八戒"],["八戒","沙僧"])
# print(name_set)
#把一个集合并与另外一个集合
# name_set.update({"张飞","李逵"})
# print(name_set)

#三种删除操作
#remove(元素)
name_set = {"zhangsan","lisi","wangwu"}
# name_set.remove("lisi")
# print(name_set)
# name_set.remove("zhangsan")
#discard(元素)
# name_set.discard("lisi")
# print(name_set)
# name_set.discard("lisi")
#pop随机删除
# name_set.pop()
# print(name_set)
#交集
num_set1 = {1,2,4,7}
num_set2 = {2,5,8,9}
# inter_set1 = num_set1 & num_set2
# inter_set2 = num_set1.intersection(num_set2)
# print(inter_set1)
# print(inter_set2)
#并集
# union_set1 = num_set2 | num_set1
# union_set2 = num_set1.union(num_set2)
# print(union_set1)
# print(union_set2)
#差集
# diff_set1 = num_set1 - num_set2
# diff_set2 = num_set1.difference(num_set2)
# print(diff_set1)
# print(diff_set2)
#对称差集
sym_diff_set1 = num_set1 ^ num_set2
sym_diff_set2 = num_set1.symmetric_difference(num_set2)
print(sym_diff_set1)
print(sym_diff_set2)