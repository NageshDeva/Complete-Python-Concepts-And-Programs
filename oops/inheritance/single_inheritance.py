#inheritance
'''Inheritance is a mechanism that allows a new class to inherit
properties & behaviour from an existing class

This means that the subclass can reuse and extend the attribute and 
methods of the superclass.

Inheritance is the ability to inherit the features/properties/Attributes/methods from a parent class to subclass.

Why inheritance?
-->code reusability
-->maintainable
-->Readibility

Types of inheritance:
1)single Inheritance
2)Multiple Inheritance
3)multilevel Inheritance
4)Hierarchical Inheritance
5)Hybrid Inheritance


syntax:- class DerivedclassName(BaseClassName):
'''
#single Inheritance:
'''The concept of inheriting the properties from one class to another class is known as single inheritance'''
class father:
    def m1(self):
        print("parent method")
class son(father):
    def m2(self):
        print("child method")

s=son()
s.m1()
s.m2()

class Human:
    def eat(self):
        print("i can eat")
    def work(self):
        print("I can work")
class male(Human):             #Reusability of code
    pass
male_1=male()
male_1.eat()
male_1.work()

class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("i can work")
class male(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("i can code")     #method overriding
m = male()   #creating object
m.flirt()    #calling method
m.work()     #calling method


class Human:
    def __init__(self,num_heart):
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart=num_heart   #New attribute
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(Human):
    def __init__(self,name,num_heart):
        super().__init__(num_heart)                     #Here we are inheriting the base class constructor.
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()                 #superkeyword access the parent class method in base class.
        print("i can code") 
    def display(self):
        print(f"Hi, Iam {self.name} and I have {self.num_heart} heart and {self.num_eyes} eyes and {self.num_nose} nose")

obj=male('shiva',1)
obj.flirt()
obj.work()
obj.display()

