#multiple Inheritance:
'''
one child class can inherits properties from more than one parent class.
syntax:
       class className(parentclass,parentclass):
       
To access the method of 2nd parent class.
syntax:
       classname.method(obj)
'''
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("i can work")
class male:
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("i can code")     
class Boy(Human, male):
    pass
b = Boy()   #creating object
b.flirt()    #calling method
b.work()     #calling method             I want to display the male class method rather than humanclass then classname.method(objname)


#class.method(objname)
class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("i can work")
class male:
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("i can code")     
class Boy(Human, male):
    pass
b1 = Boy()   #creating object
b1.flirt()    #calling method
b1.work()
male.work(b1)     #To access the method of 2nd parent class.