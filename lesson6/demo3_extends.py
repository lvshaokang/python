'''
多继承
'''
class AI:
    def face(self):
        print("人脸识别")
    def data_ana(self):
        print("AI数据处理")

class BigData:
    def data_ana(self):
        print("BigData数据分析")

class Python(AI,BigData):
    def opertation(self):
        print("自动化运维")


# py = Python()
# py.data_ana()
# py.face()
# py.data_ana()
# py.opertation()

#多态
class Animal:
    def eat(self):
        print("Animal 正在吃饭")

class Dog(Animal):
    def eat(self):
        print("Dog正在吃饭")

class Cat(Animal):
    def eat(self):
        print("Cat正在吃饭")

def show_eat(obj):
    obj.eat()

wangcai = Dog()
show_eat(wangcai)
tom = Cat()
show_eat(tom)