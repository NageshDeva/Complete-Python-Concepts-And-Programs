"""A function is a block of code which only runs when it is called.
it consists of parameters at the time of calling function we have to give Arguments/values to the function.
Advantage of functions code reusability."""

#parameters :--> Are the inputs to the function. if function contain parameters, then while calling function we should provide values.

def wish(name):
    print("hello", name, "good morning")

wish("Nagesh")
wish("shiva")

#Return :--> functions can take input values as parameters and executes business logic, and returns output to the caller with return statement.
def add(x,y):
    print(x+y)
add(5,6)

def sub(d,b):
    return d-b
result = sub(10,5)
print("the sub is", result)

def number(n):
    if n%2 == 0:
        print(n,"it is a even number")
    else:
        print(n,"it is a odd number")

number(10)
number(5)


def fact(n):
    fact = 1
    while n>=1:
        fact = fact * n
        n=n-1
    return fact
result2=fact(5)
print(result2)

#Returning multiple values
def sum_sub(a,b):
    sum = a + b
    sub = a - b
    return sum, sub
x,y = sum_sub(10,2)
print("The sum is", x)
print("the sub is", y)


def calc(a,b):
    sum = a + b
    sub = a - b
    div = a / b
    mul = a * b
    return sum, sub, mul, div
p = calc(100,50)
print("The results are ")
for i in p:
    print(i)


#Types of Arguments
#positional Argument --> These are arguments passed to function in correct positional order.
def sub(a,b):
    print(a-b)
sub(100,200)
"""no.of arguments & position of arguments must be matched if we change the order then result may be changed.
if we change no.of arguments then we will get error."""

#keyword Argument --> we can pass argument values by keyword i.e., by parameter name
"""Note: order of arguments not important but no.of arguments should be matched."""
def wish(name,msg):
    print("Hello,",name, msg)
wish(msg="Good Evening.!", name="Nagesh")
wish(name="shiva", msg="Good Morning.!")
#positional Arguments followed by keyword Arguments.
wish("charan",msg="good Afternoon.!")


#Default Argument --> sometimes we can provide default values for our positional arguments

def salute(name="Guest"):
    print(name,"Welcome to the world of python")
salute("Naveen")
salute()

"""if we are not passing any name then only default value will be considered.
non-default arguments follows default arguments."""

#variable length arguments:
"""sometimes we can pass variable no.of arguments to our function.
we declare variable length arguments with * symbol  def f1(*n)
we can call this function by passing any no.of arguments including zero number

** internally all this values represented in the form of tuple."""

def sum(*n):
    total = 0
    for i in n:
        total = total + i
    print("the sum is ", total)

sum(10,20,30,40,50)

# we can mix variable length arguments with positional arguments
def f1(n1, *s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10)
f1(10,20,30,40)
f1(1,"a","b",30,70)

#After variable length argument if we are taking any other argument then we should provide values as keyword arguments.
def f2(*s, n1):
    for s1 in s:
        print(s1)
    print(n1)
f2("A","B", n1=10)


#Keyword variable length arguments
"""for this we use **
we can call this function by passing any no.of keyword arguments internally these keyword arguments will stored inside a dictionary."""
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=100,n2=200,n3=300)
display(rno=101, name="nagesh", marks=90, subject="social")

#Anonymous function:
"""sometimes we can declare a function without any name such type of nameless functions are called anonymous function or lambda function."""
#lambda function:
"""A lambda function can take any no.of arguments but can only have one expression.

using lambda we can write very concise code. so that readability of program will be improved."""
#square of a given number.
s=lambda n:n*n
print("the square of 4 is",s(4))
print("the square of 5 is",s(5))

#sum of 2 given numbers.
s= lambda a,b : a + b
print("The sum of a,b is:",s(10,20))
print("The sum of a,b is:",s(100,20))

#biggest of given values
s=lambda a,b: a if a>b else b
print("The Biggest of 10, 20 is:", s(10,20))

#filter
"""To filter values from the given sequence based on some condition"""
def isEven(x):
    if x%2 == 0:
        return True
    else:
        return False
l = [0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)

l = [0,5,10,15,20,25,30]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)


#map()
"""for every element present in the given sequence apply some functionality and generate new element with required modification
for this requirement we should go for map() function"""

l2 = [1,2,3,4,5]
def double(x):
    return 2*x
l21 = list(map(double,l2))
print(l21)

l = [1,2,3,4,5]
l1=list(map(lambda x: 2*x,l))
print(l1)

m=[1,2,3,4,5]
m1 = list(map(lambda x: x*x, m))
print(m1)

#Reduce function()
"""reduce function reduces sequence of elements into a single element by applying specified function.
reduce function present in functools module we should import functools module"""
from functools import*
l = [10,20,30,40,50]
result = reduce(lambda x,y : x+y,l)
print(result)

result= reduce(lambda x,y: x*y,l)
print(result)

from functools import*
result = reduce(lambda x,y: x+y,range(1,101))
print(result)


