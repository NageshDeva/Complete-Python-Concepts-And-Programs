Tuple = (1,3,4,5,6,7)
print(Tuple)
print(type(Tuple))


"""index(): indexing to know the element position in the tuple"""
t = (1,3,4,5,6,7)
print(t[0])
print(t[1])
print(t[-1])

"""slice(): sclice operator is used to accessing a part of tuple. """
t = (1,3,4,5,6,7,8,2,44,77,88,96,32)
print(t[1:])
print(t[1:5])
print(t[1: :2])
print(t[-5:-1])

""" t= (10,20,30,40)
    t[1]= 70 ---->type error 'tuple' object doesnot support item assignment."""
#concatenation operator
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1 + t2
print(t3)

#Multiplication operator:
t11 = (10,20,30)
t22 = t11*3
print(t22)

"""len(): This operator is used to find the length of a tuple"""
t12 = (10,20,30)
print(len(t12))

"""count(): to returns no.of occerrence of a given element in the tuple"""
t22=(10,20,30,40,20,10,10)
print(t22.count(10))

"""sorted(): to sort elements based on natural sorting order. & returns in a list."""
tt = (10,40,26,1,40,57,80,70)
ts = sorted(tt)
print(ts)

# sort acc to reverse order also.
ttt = (10,40,26,1,40,57,80,70)
trs = sorted(ttt, reverse=True)
print(trs)

"""min() & max() functions: returns min and max values acc to default natural sorting order."""
tup = (10,40,26,1,40,57,80,70)
print(min(tup))
print(max(tup))

""" Tuple packing and unpacking"""
#tuple packing
a=10
b=20
c=30
d=40
tupl= a,b,c,d
print(tupl)

#tuple unpacking
tu = (10,20,30,40)
a,b,c,d = tu
print("a=",a, "b=",b, "c=", c, "d=",d)

