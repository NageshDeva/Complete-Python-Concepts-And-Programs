# Class--> is a blue print of an object. it consists both properties and methods.
"""properties--> can be represented by variables.
methods--> can be represented by Actions"""
class student:
    def __init__(self):
        self.name='shiva'
        self.age=40
        self.marks=80
    
    def talk(self):
        print("hello Iam :", self.name)
        print("my age is:",self.age)
        print("my marks are:", self.marks)

#object --> physical existence of a class is nothing but object.
        '''object is instance of a class
We can create any no.of objects for a class.
object creation--> reference_variable = classname()
method--> reference_variable.methodname()'''

class student:
    def __init__(self):
        self.name='shiva'
        self.age=40
        self.marks=80
    
    def talk(self):
        print("hello Iam :", self.name)
        print("my age is:",self.age)
        print("my marks are:", self.marks)
s1 = student()
s1.talk()


#self--> it always pointing to current object.
'''By using self we can access instance variables and instance objects.'''

#Constructor--> special method in python
'''constructor is automatically executed at the time of object creation.
The main purpose of constructor is to declare and initialize instance variables.
per object constructor will be executed only once.'''

class Test:
    def __init__(self):
        print("constructor execution....")
    
    def m1(self):
        print("method execution....")

t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()


class school:
    def __init__(self,x,y,z):
        self.name = x
        self.rollno = y
        self.marks = z
    def display(self):
        print(f"student Name: {self.name}\n Rollno:{self.rollno}\n Marks:{self.marks}")
    
s11 = school("Nagesh",26, 89)
s11.display()
s12 = school("Charan",27, 92)
s12.display()
