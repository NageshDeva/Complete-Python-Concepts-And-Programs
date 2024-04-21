#overloading
'''we can use same operator or methods for different purposes.
 + operator is used for Airthematic addition and string concatenation.
  print(10+20)#30
  print('Nagesh'+'Deva')#NageshDeva
 * operator is used for multiplication and string repetition purposes.
  print(10*20)#200
  print('deva'*3)#devadevadeva

We can use deposit() method to deposit cash or cheque or dd.
deposit(cash)
deposit(cheque)
deposit(dd)

3 types of overloading.
1.operator overloading
2.method overloading
3.constructor overloading
'''
#1.Operator Overloading.
'''We can use same operator for different purposes,which is nothing but operator overloading.
python supports operator overloading.'''

"""class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
b2=Book(200)         #trows error Book class doesnt know wt to do 
print(b1+b2)"""

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(100)
b2=Book(200)
print('The Total no.of pages:',b1+b2)

#method overloading
'''if two methods having same name but different type of arguments then those methods are
said to be overloaded methods.

-->but in python 'method overloading is not possible'.

-->if we are trying to declare multiple methods with same name different
number of arguments then python will always consider only last method.'''
class Test:
    def m1(self):
        print('No argument method.')
    def m1(self,a):
        print('one-argument method.')
    def m1(self,a,b):
        print('two argument method.')
t=Test()
#t.m1()     #Error req 2 positional args
#t.m1()    #Error req 2 positional args
#t.m1(10,20)

#in this program python will consider only last method.
'''
we can handle overloaded method requirements in python:
if method with variable no.of arguments required then we can 
handle with default arguments or with variable no.of argument methods.
'''
class Test1:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The sum is:',total)
t2=Test1()
t2.sum(10,20)
t2.sum(10,20,30)
t2.sum(10)
t2.sum()

#constructor Overloading:
'''
'constructor overloading is not possible' in python
if we define multiple constructors then the last constructor will be considered.
'''
class Navaneeth:
    def __init__(self):
        print('No arg constructor')
    def __init__(self,a):
        print('one argument constructor.')
    def __init__(self,a,b):
        print('Two Argument constructor')

#g=Navaneeth()      #error missing 2 args
#g=Navaneeth(500)   #error missing 2 args
g=Navaneeth(500,300)

#constructor with Default Arguments:
class shiva:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 no.of arguments')

s=shiva()
s1=shiva(10)
s2=shiva(10,20)
s3=shiva(10,20,30)

#constructor with variable no.of arguments:
class Naveen:
    def __init__(self,*v):
        print('constructor with variable no.of arguments')
n=Naveen()
n1=Naveen(23)
n2=Naveen(23,33,44)
n3=Naveen(44,55,6,7,8,7,89,9)