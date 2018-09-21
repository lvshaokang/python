'''
继承
'''

class Animal:
    def __private(self):
        print("私有方法!")
    def eat(self):
        print("---吃-----")
    def drink(self):
        print("----喝-----")
    def run(self):
        print("----跑-----")


class Dog(Animal):
    def hand(self):
        print("*******握手*******")
    # 重写
    def run(self):
        print("摇着尾巴跑！")


class GoldenDog(Dog):
    def guide(self):
        Dog.hand(self)
        print("我能导航!")

wangcai = Dog()
wangcai.run()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.hand()
# wangcai.__private()

duoduo = GoldenDog()
duoduo.guide()
duoduo.hand()
duoduo.eat()
duoduo.run()