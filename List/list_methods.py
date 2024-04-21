L = [1,2,3,4,2,'nagesh', True, 3.5 ]
print(L)
print(type(L))

#Accessing List elements.
"""Index(): it is used to access each element in the list using its positions or vice versa"""
L = [1,2,3,4,2,'nagesh', True, 3.5 ]
print(L[0])
print(L[1])
print(L[7])
print(L[-1])

"""slice(start: stop: step): it is used to extract a small part of a list """
L = [1,2,3,4,2,'nagesh', True, 3.5 ]
print(L[1:])
print(L[1:4])
print(L[:4])
print(L[1: :2])

"""len(): Returns the no.of elements present in list."""
n =[10,20,30,40,50]
print(len(n))

"""count(): returns the no.of occurences of specified item in the list."""
m = [1,2,3,4,5,1,2,3,1,8,9,1]
print(m.count(1))

#manipulating
"""append(): we can use append function to add item at end of list"""
list = ['A','B','C']
list.append(1)
list.append("m")
print(list)

listt = []
for i in range(101):
    if i%10 == 0:
        listt.append(i)
print(listt)

"""insert(): To insert item at specified index position"""
lis = [1,2,3,4,5,6,7,8]
lis.insert(2,566)
print(lis)
lis.insert(-1, 43)
print(lis)
print(lis[-1])

"""extend(): to add all items of one list to another list."""
n = [1,2,3,4]
np = [5,6,7,8]
n.extend(np)
print(n)


"""remove(): use this function to remove specified item from the list."""
ml = [1,2,3,4,5,6,7,"nagesh"]
ml.remove("nagesh")
print(ml)      

"""pop(): it removes and returns the last element of the list"""
mla = [1,2,3,4,5,6,7,"nagesh", "deva"]
mla.pop()
print(mla)


#ordering the elements.

"""reverse(): we can use to reverse order of elements of a list"""
npm = [1,2,3,4,5,6]
npm.reverse()
print(npm)

"""sort(): we can sort elements in list.
   --> Acc to default natural sorting order 
   --> for numbers Ascending order 
   --> alphabets Alphabetical order
   
   To use sort compulsory list elements should be homogenous."""
v = [1,76,36,22,90,65,39,47,88,888,333,154,91]
v.sort()
print(v)

alpha = ["nagesh", "deva", "shiva", "naveen", "charan"]
alpha.sort()
print(alpha)


"""copy(): this function is ment for cloning."""
x = [10,20,30,40]
y=x.copy()
print(y)


#mathematical operators
"""concatenation operator(+): we use + to concatenate 2 lists into single list."""
c = [10,20,30,40]
d = [50,60,70,80]
e=c+d
print(e)

g=e+[90]
print(g)

"""Repetation operator(): to repeat elements of specified no.of items."""
t = [5,6,7,8]
z = t*3
print(z)


"""clear(): clear function to remove all elements of list."""
b = [66,44,77,55,12]
b.clear()
print(b)

#nested list
dd = [10,20,30,[40,50,60],70]
print(dd)
print(dd[0])
print(dd[3])
print(dd[3][0])

#list comprehensions:
"""it is very easy and compact way of creating list objects from any iterable objects."""
s = [x*x for x in range(1,11)]
print(s)

v= [2**x for x in range(1,6)]
print(v)


j = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
mk = [x for x in j if(x%2==0)]
print(mk)

Names = ["naveen", "charan", "shiva", "Nagesh"]
l=[w[0] for w in Names]
print(l)

