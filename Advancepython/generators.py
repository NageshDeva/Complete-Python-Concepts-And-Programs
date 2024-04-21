#Generator
'''Generator is a function which is responsible to generate a sequence of values.

we can write generator functions just like ordinary functions, but it uses yield keyword to return values.'''

#Advantages:
'''
1) Generators are easy to use.
2) improves memory utilization and performance.
3) sutiable for reading data from large no.of large files.
'''
def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))


def countdown(num):
    print("start Countdown")
    while num>0:
        yield num      #returns the value of num each time through the loop, This turns the function into generators.
        num = num - 1
values = countdown(5)
for x in values:
    print(x)


#to generate first n numbers.
print("-------firstn numbers--------")
def firstn(num):
    n=1
    while n<=num:
        yield n
        n = n + 1
values1 = firstn(10)
for y in values1:
    print(y)

print("----fibonacci Numbers-----")

def fib():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b
for f in fib():
    if f > 100:
        break
    print(f)



import random

names = ['sunny', 'bunny', 'tiger', 'sugar']
subjects = ['python','c','php']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id':i,
            'name': random.choice(names),
            'subjects': random.choice(subjects)
            }
        result.append(person)
    return result

people = people_list(5) 
print(people)