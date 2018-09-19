#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
json和csv文件操作
'''
import json
import csv

# dict = {"name":"zhangsan","age":20,"language":("python","java"),"study":{"AI":"python","bigdata":"hadoop"},"if_vip":True,"gender":None}
# json_str = json.dumps(dict)
# print(json_str)
# py_dict = json.loads(json_str)
# print(py_dict)
# print(type(py_dict))
# #dump向json文件写内容
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info.json","w") as f:
#     json.dump(dict,f)
# load加载json文件
'''
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info.json","r") as f:
#     user_info_data = json.load(f)
#     print(user_info_data)
#     print(type(user_info_data))
'''
datas = [["name", "age"], ["zhangsan", 20], ["lisi", 30]]
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info.csv","w",newline="",encoding="utf-8") as f:
#     writer = csv.writer(f)
#     # for row in datas:
#     #     writer.writerow(row)
#     # 一次写入多行
#     writer.writerows(datas)
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info.csv","r",newline="",encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#         print(row[0])
#         print(row[1])
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info.csv","r",newline="",encoding="utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     print(header)
#     print("---------------------")
#     for row in reader:
#         print(row)
#         print(row[0])
#         print(row[1])

# 字典数据操作
header = ["name", "age"]
rows = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}]
# with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info2.csv","w",newline="",encoding="utf-8") as f:
#     writer = csv.DictWriter(f,header)
#     writer.writeheader()
#     writer.writerows(rows)

with open("D://lamp/SourceCode/bigdata/test/python/lesson5/user_info2.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row["name"], row["age"])
