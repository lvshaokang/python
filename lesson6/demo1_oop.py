'''
构造方法
'''

'''
class Dog:
    # 无参构造方法
    # def __init__(self):
    #     print("我是构造方法，在创建对象的时候自动调用！")
    # 带参构造方法
    def __init__(self, g, v, n):
        self.gender = g
        self.variety = v
        self.name = n

    def get_pro(self):
        print("我的名字是：{}".format(self.name))

    def eat(self):
        print("正在啃骨头。。。")

    def drink(self):
        print("正在喝水。。。")


# wangcai = Dog()
wangcai = Dog("male", "golden", "wangcai")
print(wangcai.gender)
print(wangcai.variety)
print(wangcai.name)
wangcai.get_pro()
'''
# wangcai.eat()
# print("------------------------")
# fugui = Dog("male","golden","fugui")
# print(fugui.gender)
# print(fugui.variety)
# print(fugui.name)

'''
class Dog:
    def __init__(self, g, v, n, a):
        self.gender = g
        self.variety = v
        self.name = n
        self.__age = a # 私有属性

    def get_pro(self):
        print("gender：{},variety:{},name:{},age:{}".format(self.name, self.variety, self.name, self.__age))

    def set_pro(self,**kwargs):
        if "gender" in kwargs:
            self.gender = kwargs["gender"]
        elif "variety" in kwargs:
            self.variety = kwargs["variety"]
        elif "name" in kwargs:
            self.name = kwargs["name"]
        elif "age" in kwargs:
            if kwargs["age"] < 0 or kwargs["age"] > 20:
                print("非法年龄：{}".format(kwargs["age"]))
            else:
                self.__age = kwargs["age"]

    def eat(self):
        print("正在啃骨头。。。")

    def drink(self):
        print("正在喝水。。。")


wangcai = Dog("male","golden","wangcai",1)
wangcai.get_pro()
wangcai.set_pro(age=3)
# wangcai.__age = 3 ## 失效
wangcai.get_pro()
'''

#私有方法
class Comrade:
    def __send_message(self): #私有方法
        print("消息已经汇报给上级")
    def answer(self,secret):
        if secret == "芝麻开门":
            print("接头成功")
            self.__send_message() #调用自身的私有方法
        else:
            print("接头失败")


c = Comrade()
c.answer("芝麻开门")




