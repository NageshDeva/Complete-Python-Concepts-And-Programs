#Hierarchical Inheritance
'''The concept of inheriting properties from one class into 
multiple classes which are present at same level is known as Hierarchical inheritance.

-->more than one derived class are created from a single base class
this type of inheritance is called Hierarchical inheritance'''

class Human:
    def __init__(self,name,age):
        print("calling init from human class")
        self.name=name
        self.age=age
    def showDetails(self):
        print(f"name:{self.name},age:{self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def sleep(self):
        print("I can sleep whole day")
class female(Human):
    def work(self):
        print("I can code")
female_1=female("Nagesh",23)
female_1.showDetails()
female_1.eat()
print(female_1.name)
print(female_1.age)
'''Female class can acess only female class attributes & methods of Human class
(parent class), it doesnt take any attribute of male class 
for male class it access only male class & Human class
Attributes & methods it doesnt access female class attributes. '''


class Human:
    def __init__(self,name,age):
        print("calling init from human class")
        self.name=name
        self.age=age
    def showDetails(self):
        print(f"name:{self.name},age:{self.age}")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,name,age,location):
        print("calling __init__ from male class")
        #Human().__init__(self,name,age)
        self.name=name
        self.age=age
        self.location=location
    def sleep(self):
        print("I can sleep whole day")
class female(Human):
    def work(self):
        print("I can code")
male_1=Male("Deva",22,"HYD")
male_1.showDetails()
male_1.eat()
male_1.sleep()
print(male_1.name)
print(male_1.age)

