'''
函数
'''
#打印固定个人信息
def print_user_info():
    print("name:zhangsan")
    print("age:20")
    print("gender:male")
# 带参函数
def print_user_info2(name,age,gender):
    print("name:{}".format(name))
    print("age:{}".format(age))
    print("gender:{}".format(gender))
# 带有返回值函数
def x_y_sum(x,y):
    res = x + y
    return res

def x_y_comp(x,y):
    rs1 = x + y
    rs2 = x - y
    rs3 = x * y
    rs4 = x / y
    rs = [rs1,rs2,rs3,rs4]
    return rs

def x_y_comp2(x,y):
    rs1 = x + y
    rs2 = x - y
    rs3 = x * y
    rs4 = x / y
    # rs = (rs1,rs2,rs3,rs4)
    return rs1,rs2,rs3,rs4


# print_user_info()
# name = "lisi"
# age = 18
# gender = "male"
# print_user_info2(name,age,gender)
# z = x_y_sum(10,40)
# print(z)

# z = x_y_comp(20,4)
# print(type(z))
z = x_y_comp2(20,4)
print(z)