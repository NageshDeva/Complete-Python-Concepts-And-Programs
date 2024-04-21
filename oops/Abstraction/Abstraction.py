#Abstarction
'''Abstraction is used to hide the irrelevant information inorder to reduce the complexity
Abstraction is a mechanism of only declaring methods but not intializing declared methods are implemented in its sub class.



we can achieve the data abstraction by using abstract classes. it can be 
created using abc (abstact base class) module and abstract method.

#Abstract class  ---> give a plan/ structure
Abstract class is a class in which one or more abstract methods are defined
when a method declared inside a class without implementation is known as Abstract method.
-->must contain 1 abstract method.
--> which have no declaration
--> using decorator

#Abstract method
To create abstract method and abstract class we have to 
import the "ABC" and "abstract method" classes from ABC library
syntax: @abstract method

** we cannot create abstract class without a abstract method & this method shouldn't 
have any declaration.

** we cannot create object of an abstract class but by removing decorator we can create 
object but it doesnt be a abstract class without an abstract method

Abstract class can have both abstract method & normal method.
'''

from abc import ABC, abstractmethod

class polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        print("I have any no.of sides")
class Triangle(polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("I have 3 sides")
class Rectangle(polygon):
    def __init__(self):
        pass
    def no_of_sides(self):
        print("I have 4 sides")

obj1 = Triangle()
obj1.no_of_sides()
obj2=Rectangle()
obj2.no_of_sides()


from abc import ABC, abstractmethod
class Robo(ABC):
    @abstractmethod
    def sana(self, eyes):
        pass
class chitti(Robo):
    def sana(self,eyes,nose,ears,hands):
        self.eyes = eyes
        self._nose = nose
        self.__ears = ears
        self.__hands=hands
        print("Hi! sana")

    def get_ears(self):
        return self.__ears 
    def get_hands(self):
        return self.__hands
    def setters_hands(self,num):
        self.__hands = num


b = chitti()
b.sana(2,1,2,2)
print(b.eyes)
print(b._nose)
#print(b.__ears)
print("This is a private variable using getters method i have ",b.get_ears(),"ears")
print("The hands I have is",b.get_hands())
print(b.setters_hands(33))
print("The hands I have is after modifing the priavte variable is",b.get_hands())