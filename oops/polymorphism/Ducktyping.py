#poly means many
#morphs means forms
'''
1. Duck typing philosophy of python
2. Overloading
     1) operator overloading
     2) method overloading
     3) constructor overloading
3. Overriding
     1)method overriding
     2)constructor overriding
'''
#Duck Typing
'''This feature mainly support Dynamic typing.
What is the type of obj? we cannot decide at the beginning. At runtime we can pass any type.
then how we can decide the type?
At runtime if 'it walks like a duck and talks like a duck, it must be duck', python follows this principle
This is called Duck typing philosophy of python.'''



'''  **************
Duck typing focuses on the capabilities of an object rather than its specific class.
If an object has the required methods or attributes to perform a task, it can be used, regardless of its actual class.
'''
class Duck:
    def swim(self):
        print('Iam a duck and i can swim')
    def speaks(self):
        print('Quack Quack')
class Dog:
    def swim(self):
        print('Iam a Dog and I can Swim.')
    def speaks(self):
        print('Boow Boow')
def display(duck):
    duck.swim()
    duck.speaks()
    print('Info Displayed')
d=Duck()
display(d)
do=Dog()
display(do)




class Duck:
    def talk(self):
        print('Quack Quack')
class Dog:
    def talk(self):
        print('Boow Boow')
class cat:
    def talk(self):
        print('Meow Meow')
class Goat:
    def talk(self):
        print('Myaah Myaah')

def f1(obj):
    obj.talk()
l=[Duck(),cat(),Dog(),Goat()]
for obj in l:
    f1(obj)

'''The problem in this apporach is if the obj does not contain talk()method then we will get AttributeError.'''

class Duck:
    def talk(self):
        print('quack quack..')

class Dog:
    def bark(self):
        print('Boow Boow..')



p=Duck()
p.talk()

#g=Dog()
#g.talk()

'''But we can solve this problem by using hasattr() function.
hasattr(obj,'attributename')--> attribute name can be method name or variable name.'''

class Duck:
    def talk(self):
        print('Quack Quack..')
class Human:
    def talk(self):
        print('Hello Hi')
class Dog:
    def bark(self):
        print('Boow Boow')

def f3(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

d1= Duck()
f3(d1)

h=Human()
f3(h)

d2= Dog()
f3(d2)

