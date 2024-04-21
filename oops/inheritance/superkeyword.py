#it will give you the access of all the attributes & methods of base class.
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("i can work")
class male(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()                 #superkeyword access the parent class method in base class.
        print("i can code")     #method overriding
m = male()   #creating object
m.flirt()    #calling method
m.work()     #calling method


#Attributes:
class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(Human):
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()                 #superkeyword access the parent class method in base class.
        print("i can code") 

g=male()
g.flirt()
g.work()
print("no.of eyes for a human is:",g.num_eyes)        #accessing Attributes of base class as  objname.attributename


'''Accessing attributes of base class to sub class by super keyword.'''
'''When sub class has constructor then to access baseclass attributes we have to use superkeyword.'''

class Human:
    def __init__(self):
        self.num_eyes = 2
        self.num_nose = 1
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class male(Human):
    def __init__(self,name):
        super().__init__()                     #Here we are inheriting the base class constructor.
        self.name = name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()                 #superkeyword access the parent class method in base class.
        print("i can code") 

v=male('shiva')
v.flirt()
v.work()
print("The no.of eyes of a human in base class through subclass object is",v.num_eyes)
print("sub class person name is:",v.name)

