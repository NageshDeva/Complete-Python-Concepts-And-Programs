#Types of methods:
'''
1.instance methods
2.class methods
3.static methods
'''

#instance method:
'''
inside method implementation if we are using instance variables then such type of methods
are called instance methods.
inside instance method declaration, we have to pass self variable. def m1(self):
By using self variable inside method we can access instance variables.
within the class we can call instance method by using self variable and from outside of the class we can call by using object reference. '''

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks = marks
    def display(self):
        print("Hi",self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks >= 60:
            print('you got first grade')
        elif self.marks >= 50:
            print('you got second grade')
        elif self.marks >= 35:
            print('you got third grade')
        else:
            print('you are failed.')
n = int(input('Enter number of students:'))
for i in range(n):
    name = input('Enter Name:')
    marks = int(input('Enter Marks:'))
    s = student(name,marks)
    s.display()
    s.grade()
    print()


#setter and getter methods:
'''we can set and get values of instance variables by using getter and setter methods.

setter method can be used to set values to the instance variables. setter methods also known as mutators methods.

def setvariable(self,variable):
    self.variable=variable.
'''
def setName(self,name):
    self.name=name

#getter Methods:
'''getter method can be used to get values of the instance variables. getter methods also known as accessor methods. 
syntax:
def getvariable(self):
    return self.variable
    
def getName(self):
    return self.name'''

class student2:
    def setName(self,name):
        self.name=name
    
    def getName(self):
        return self.name
    
    def setMarks(self, marks):
        self.marks=marks
    
    def getMarks(self):
        return self.marks
n2 = int(input('Enter no.of students:'))
for i in range(n2):
    s2=student2()
    name=input('Enter Name:')
    s2.setName(name)
    marks=int(input('Enter Marks:'))
    s2.setMarks(marks)

    print('Hi',s2.getName())
    print('your marks are:', s2.getMarks())
    print()

#class Methods:
    '''inside method implementation if we are using only class variables(static variables),
    then such type of methods we should declare as class method.
    we can declare class method explicitly by using @classmethod decorator.
    for class method we should provide cls variable at the time of declaration
    we can call classmethod by using classname or object reference variable.'''

class Animal:
    legs =4
    @classmethod
    def walk(cls,name):
        print(f'{name} walks with {cls.legs} legs..')
Animal.walk('Dog')
Animal.walk('Cat')

#program to track the no.of objects created for a class.
class Test:
    count=0
    def __init__(self):
        Test.count=Test.count+1
    @classmethod
    def noofobjects(cls):
        print('The no.of objects created for test class:', cls.count)
t1=Test()
t2=Test()
Test.noofobjects()
t3=Test()
t4=Test()
t5=Test()
Test.noofobjects()

#static methods:
'''
1.in general these methods are general utility methods.
2.inside these methods we wont use any instance or class variables.
3.here we wont provide self or cls arguments at the time of declaration
we can declare static method explicitly by using @staticmethod decorator
we can access static methods by using classname or object reference.
'''
class shiv:
    @staticmethod
    def add(x,y):
        print('the sum:',x+y)
    @staticmethod
    def product(x,y):
        print('The product:',x*y)
    @staticmethod
    def average(x,y):
        print('The average:',(x+y)/2)

shiv.add(10,20)
shiv.product(10,20)
shiv.average(10,20)



#passing members of one class to another class:

class Employe:
    def __init__(self,eno,ename,esal):
        self.eno = eno
        self.ename = ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee salary:',self.esal)
class Test1:
    def modify(emp):
        emp.esal = emp.esal+10000
        emp.display()
e = Employe(100,'Navaneeth',10000)
Test1.modify(e)