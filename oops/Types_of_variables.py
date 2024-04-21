#instance variables (object Level variable)
#static variables (Class Level variable)
#Local Variables (Method Level Variables)

#instance variable:
'''if the value of a variable is varied from object to object, then such type of variables are instance variables.
Where we can declare instance Variables:
1.inside constructor by using self variable.
2.inside instance method by using self variable.
3.outside of the class by using object reference variable.'''

#inside constructor by using self variable:
'''We can declare instance variables inside a constructor by using self keyword.
once we create object, automatically these variables will be added to the object'''

class Employee:
    def __init__(self):
        self.eno=100             #inside constructor
        self.ename='Nagesh'       
        self.esal=25000
e=Employee()
print(e.__dict__ )


#inside instance method by using self variable.
'''We can declare instance variables inside instance method by using self variable.
if any instance variable declared inside instance method, that instance variable will be
added once we call that method.'''

class Test:
    def __init__(self):
        self.a=10
        self.b=20

    def m1(self):
        self.c=30         #instance method variable
t=Test()
t.m1()
print(t.__dict__)

#outside of the class by using object reference variable.
'''we can also add instance variables outside of a class to a particular object.'''
class Test2:
    def __init__(self):
        self.a=10
        self.b=20
    def m1(self):
        self.c=30
t1=Test2()
t1.m1()
t1.d=40      #outside of the class instance variable
print(t1.__dict__)


#How to access instance variables:
'''we can access instance variables with in the class by using self variable
and outside of the class by using object reference.'''

class Hello:
    def __init__(self):
        self.a=100
        self.b=200
    def display(self):
        print(self.a)
        print(self.b)
h = Hello()
h. display()
print(h.a,h.b)              #Accessing instance variables.

#How to delete instance variable from the object.
'''within a class we can delete instance variable as follows
    del self.variableName'''


class shiva:
    def __init__(self):
        self.a=22
        self.b=23
        self.c=24
        self.d=25
    def d1(self):
        del self.d     #within a class del
f = shiva()
print(f.__dict__)
f.d1()
print(f.__dict__)

'''From outside of class we can delete instance variables as follows:
    del objectreference.VariableName'''
class shiva:
    def __init__(self):
        self.a=22
        self.b=23
        self.c=24
        self.d=25
    def d1(self):
        del self.d
f = shiva()
del f.c                 #outside of the class
print(f.__dict__)

'''Note: The instance variables which are deleted from one object, will not be deleted from other objects.'''
class shiv:
    def __init__(self):
        self.a=32
        self.b=33
        self.c=34
        self.d=35
g=shiv()
g1=shiv()
del g.a
print(g.__dict__)
print(g1.__dict__)



'''if we change values of instance variables of one object then those changes wont be refelected
to the remaining objects, because for every object
we have seperate copy of instance variables are available.'''

class charan:
    def __init__(self):
        self.a = 55
        self.b = 65

c = charan()
c.a=555
c.b=666
cd = charan()
print('c:',c.a,c.b)
print('cd',cd.a,cd.b)



#static Variables: 
'''if the values of a variable is not varied from object to object.
such type of variables we have to declare with in class directly but outside
of methods.such type of variables are called static variables.

for total class only one copy of static variable will be created and shared by all objects of that class.
'''

class Test3:
    x=10                              #static variable
    def __init__(self):
        self.y=20
t1 = Test3()
t2 = Test3()

print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test3.x = 888
Test3.y = 999
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

#various places to declare static variables:
'''
1.Declare within the class directly but from outside of any method.
2.inside constructor using class name.variablename
3.inside instance method using class name.variablename
4.inside class method by using either class name or cls variable.
5.inside static method by using class name.variablename
'''
class Navaneeth:
    a=100                   #static variable
    def __init__(self):
        Navaneeth.b=200     #static variable within constructor.
    def m1(self):
        Navaneeth.c=300     #static variable within instance method.
    @classmethod
    def m2(cls):
        cls.d1=400            #static variable with cls.variablename
        Navaneeth.d2=400      #static variable with className.variableName.
    @staticmethod
    def m3():
        Navaneeth.e=500
print(Navaneeth.__dict__)
N=Navaneeth()
print(Navaneeth.__dict__)
N.m1()
print(Navaneeth.__dict__)
Navaneeth.m2()
print(Navaneeth.__dict__)
Navaneeth.m3()
print(Navaneeth.__dict__)
Navaneeth.f=600
print(Navaneeth.__dict__)


#How to access static variables:
'''
1.from outside of class: by using either object reference or classname.
2.inside constructor: by using either self or classname.
3.inside instance method: by using either self or class name.
4.inside class method: by using either cls variable or class name.
5. inside static method: by using classname.
'''
class Naveen:
    a=101
    def __init__(self):
        print(self.a)       #Accessing static variable to constructor.
        print(Naveen.a)     #Accessing static variable to constructor.
    def m1(self):
        print(self.a)       #Accessing static variable to method.
        print(Naveen.a)     #Accessing static variable to method.
    @classmethod
    def m2(cls):
        print(cls.a)        #Accessing static variable to class method.
        print(Naveen.a)     #Accessing static variable to class method.
    @staticmethod
    def m3():
        print(Naveen.a)     #Accessing static variable to static method.
N1 = Naveen()
print(Naveen.a)    #Acessing using class Name
print(N1.a)        #Accessing using Reference variable.
N1.m1()
N1.m2()
N1.m3()

#where we can modify the value of static variable.
'''Anywhere either within the class or outside of class we can modify
by using classname. But inside class method, by using cls variable.'''

class Demo:
    f=1000
    @classmethod
    def m1(cls):
        cls.f=2000
    @staticmethod
    def m2():
        Demo.f=3000
print(Demo.f)
Demo.m1()
print(Demo.f)
Demo.m2()
print(Demo.f)

'''if we change the value of static variable by using either self or object reference
variable, then the value of static variable wont be changed, just new instance variable 
with that name will be added to that particular object.
 '''

class ff:
    a=350
    def m1(self):
        self.a=450
fff =ff()
fff.m1()
print(ff.a)             #static variable
print(fff.a)            #modified static variable.


class sd:
    x = 10
    def __init__(self):
        self.y=20
s1 = sd()
s2 = sd()
print('s1:',s1.x,s1.y)
print('s2:',s2.x,s2.y)
s1.x=76
s1.y=86
print('s1:',s1.x,s1.y)
print('s2:',s2.x,s2.y)

#How to delete static variables of a class.
'''
1.we can delete static variables from anywhere by using the following syntax.
   del classname.variablename
2.But inside classmethod we can also use cls variable.
   del cls.variablename
'''

'''class gd:
    p=10                  #static variable
    @classmethod
    def m1(cls):
        del cls.a         #deleting static variable in class method.
gd.m1()
print(gd.__dict__)'''    # Attribute Error a

'''We can modify or delete static variables only by using classname or cls variable.'''


#Local Variables:
'''to meet temporary requirements we declare variables inside method directly
such type of variables are called local variable or temporary variable.

--> Local variables will be created at the time of method execution & destroys once method completed.

--> Local variables of a method cannot be accessed from outside of a method.'''

class sunny:
    def m1(self):
        a=12            #local Variable
        print(a)
    def m2(self):
        b=13             #local variable
        print(b)
x = sunny()             #object creation
x.m1()                 #calling method m1
x.m2()                 #calling method m2

class sunny1:
    def m1(self):
        a=10000
        print(a)
    def m2(self):
        b=20000
       #    print(a)     #Name error a local variable of other method cant be accessed in other method
        print(b)
x1 = sunny1()
x1.m1()
x1.m2()
