#Multi-Level Inheritance
'''The concept of inheriting the properties from multiple classes to single class
with the concept of one after the other is known as multilevel inheritance.'''
'''
in multilevel inheritance features of base class 
and derived class are inherited into new derived class. 
'''

class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(Human):
    def sleep(self):
        print("I can sleep whole day")
class Boy(male):
    def work(self):
        super().work()
        print('I can code')
class programmer(Boy):
    def work(self):
        print("I can write programs")

b1 = Boy()
b1.work()
p1 = programmer()
p1.work()

class Human:
    def __init__(self, num_heart):
        print("calling __init__ from Human class")
        self.eyes=2
        self.num_heart=num_heart
    def eat(self):
            print("I can eat")
    def work(self):
            print("I can work")
class male(Human):
    def sleep(self):
        print('I can sleep whole day')
class Boy(male):
    def work(self):
        super().work()
        print("I can code")
boy_1 = Boy(1)
print(boy_1.eyes)
print(boy_1.num_heart)
boy_1.work()


class Human:
    def __init__(self, num_heart):
        print("calling __init__ from Human class")
        self.eyes=2
        self.num_heart=num_heart
    def eat(self):
            print("I can eat")
    def work(self):
            print("I can work")
class male(Human):
    def __init__(self, name):
         print("calling init from male class")
         self.name = name
    def sleep(self):
        print('I can sleep whole day')
class Boy(male):
    def __init__(self, heart, name, can_dance):
        super().__init__(name)
        self.num_heart = heart
        self.know_dance = can_dance 
    def work(self):
        super().work()
        print("I can code")
bb1 = Boy(1,'Nagesh',True)
print(bb1.name)
print(bb1.know_dance)
print(Boy.mro())