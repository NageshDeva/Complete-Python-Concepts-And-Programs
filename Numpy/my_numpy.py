#Numpy
'''
Numpy is a Python library used for numerical computing. It provides support for large, multi-dimensional arrays and matrices, 
along with a collection of mathematical functions to operate on these arrays efficiently. Think of it as a powerful tool
for crunching numbers and doing complex calculations with ease.
'''
import numpy as np
#python list can store only  1 dimensional type of data & that data can be of any type.
print("This is list")
lst = [1,2,3,4,5]
print(lst)

#Advantages of Numpy array over lists
#single dimensional Array
print('1D-Array')
a= np.array([1,2,3,4,5])
print(a)

#Multidimensional Array
print("2D array")
b=np.array([[1,2,3,4,5],
            [6,7,8,9,10]])
print(b)

print("3D-Array")
c=np.array([[[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]]])
print(c)


print("type of a,b,c")
print(type(a))
print(type(b))
print(type(c))

#size : Tells about no.of elements in that array.
print(' no.elements in array a is:',a.size)
print(' no.elements in array b is:',b.size)
print(' no.elements in array c is:',c.size)

#shape=(rows,columns)
print("The shape of a is:",a.shape)
print("The shape of a is:",b.shape)
print("The shape of a is:",c.shape)

#dtpe = type of data present in the array.
print("The type of data present in a is:",a.dtype)
print("The type of data present in b is:",b.dtype)
print("The type of data present in c is:",c.dtype)

d=np.array([[1,2,3,4.2,5],
             [6,7,8.9,9,10],
             [11,12,13,14,15]])
print("The data type of d is:",d.dtype)

#arr.transpose
#transpose replace the columns with rows & rows with columns.
print("The transpose of d is:",d.transpose())

#np.empty((rows,columns),dtype)
print("Randomly picked values with the size of in tuple  & dtype as mentioned below.")
print("int type\n",np.empty((4,3), dtype = int))
print("float type\n",np.empty((4,3), dtype = float))

#np.ones((rows,columns), dtype)  #float is default dtype
x = np.ones(6)
print("An array with 6 values of 1's \n",x)
y = np.ones((3,5), dtype=int)
print("An array with 3 rows & 5 columns with 1's \n", y)

#np.zeros((rows,columns),dtype)
z = np.zeros(4)
print("An array of zeros with size of 4 with default dtype of float.\n",z)

z1 = np.zeros((3,4), dtype=int)
print("An array with zeros of 3 rows and 4 columns of int type.\n",z1)

z2 = np.zeros((3,4), dtype=str)
print("An array with zeros of 3 rows and 4 columns of str type.\n",z2)

z3 = np.zeros((3,4), dtype=bool)   #Here np.zeros with bool type means false 0 is false 1 means true np.ones bool type gives you true.
print("An array with zeros of 3 rows and 4 columns of bool type.\n",z3)


#np.arange(start,end,step) it is mostly used in every data analysis.
a1 = np.arange(1,20)
print("arange function with 1 to 20 values\n",a1)

a12 = np.arange(1,20,2)
print("arange function with 1 to 20 values & with a step of 2.\n",a12)

#arr.reshape((rows,columns))
print("By using arr.reshape we can reshape a matrix into rows and columns that we need.")
p = np.arange(2,20,2)
print(p.reshape((3,3)))

m = np.arange(1,100,2)
print(m.reshape(10,5))

#arr.flatten it is inverse of reshape it is going to give single dimension array.
print("Flatten array of m is:\n",m.flatten())


#a.ravel
'''
The work of flatten and ravel is same, but in ravel if you change the current array then orginal array 
will also be changed
Ravel is faster bcoz it doesnt occupy any memory.
when coming to flatten the original array aint be changed, but the modifications can be done to the array. 
'''

#array slicing operations
print("array slicing operations")
gw = np.arange(1, 51).reshape(10, 5)
print(gw)
print("The 0th row of array gw is:\n", gw[0])  # Slice to get the first row
print("The 2nd row of array gw is:\n ", gw[2])
print("The 1st element of gw array is:\n",gw[0,0])
print("The 3rd row 4th element of gw array is:\n",gw[3,4])
print("The 2nd to 5th row elements of gw array is:\n",gw[2:5])
#only columns
print("The 2nd column of gw array is:\n",gw[:,2])
#certain rows with specified columns
print("The 2nd row to 5th row only 4th row of gw array is:\n",gw[2:5, 4])
#certain columns 
print("The 2nd col to 5th col of all elements in gw array is:\n",gw[:, 2:5])


#mathmatical operations
f = np.arange(0,18).reshape((6,3))
s = np.arange(20,38).reshape((6,3))
print(f)
print(s)
print("The addition of above two matrics would be\n",np.add(f,s))
print("The substraction of above two matrics would be\n",np.subtract(f,s))
print("The multiplication of above two matrics would be\n",np.multiply(f,s))
print("The division of above two matrics would be\n",np.divide(f,s))

print("the max of s is",s.max())
print("the min of s is",s.min())
print("the sum of s is",np.sum(s))
print("The sum of each row is:",np.sum(s, axis = 1))
print("The mean of s is:",np.mean(s))
print("The sqrt of s is:",np.sqrt(s))
print("The standard deviation of s is:",np.std(s))
print("The log of s is:",np.log(s))


import matplotlib.pyplot as plt 
plt.style.use('dark_background')
np.pi 
print("The value of sin 90 is:",np.sin(np.pi/2))   #90 degrees
print("The value of sin 30 is:",np.sin(np.pi/6))   #30 degrees
print("The value of cos 90 is:",np.cos(np.pi/2))   #90 degrees
print("The value of tan 90 is:",np.tan(np.pi/2))   #90 degrees
print("The value of tan 0 is:",np.tan(0))   #90 degrees
#using matplotlib with numpy
j=np.arange(1,11)
k=np.arange(10,110,10)

plt.figure(figsize = (6,6))
plt.plot(j,k, 'r--')
plt.show()

x_sin = np.arange(0,2*np.pi, 0.1)
y_sin = np.sin(x_sin)
print(y_sin)

plt.figure(figsize=(6,6))
plt.plot(x_sin, y_sin)
plt.title('sin curve')
plt.show()