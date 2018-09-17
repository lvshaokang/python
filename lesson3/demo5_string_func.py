'''
字符串常用内置方法
'''
#find
line = "hello world hello python"
# print(line.find("hello",6))
# print(line.find("java"))
#count
# print(line.count("world"))
#replace
# new_line = line.replace("hello","hi",1)
# print(new_line)

#split
# line_list = line.split(" ")
# print(line_list)

#starswith 用于检查字符串是否是以指定子字符串开头
#endswith  用于检查字符串是否是以指定子字符串结尾
# files = ["20171201.txt","20180101.log","20180101.txt"]
# for file in files:
#     if file.startswith("2018") and file.endswith("log"):
#         print("2018年待处理日志：{}".format(file))

#upper lower
content = input("是否继续，继续输入yes，退出输入no")
if content.lower() == "yes":
    print("欢迎继续使用")
else:
    print("退出成功，请取卡")