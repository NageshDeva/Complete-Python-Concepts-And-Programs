"""Any sequence of characters either within single quotes or double quotes is considered as a string."""
s = "shiva"
s = "sai"
print(type(s))

#multiline string:
x = '''shiva\'s software 
       solutions
       pvt ltd'''
print(x)

#Accessing Characters.
s = "shiva"
print(s[0])
print(s[3])
print(s[-1])
print(s[-3])


"""s = input("Enter some string:")
i=0
for x in s:
    print("The character present at positive index {}, and at negative index {} is {}".format(i,i-len(s),x))
    i=i+1"""

#slice operator
s = "Learning python is very easy!!"
m=s[1:7:1]
print(m)

g=s[::-1]
print(g)

#Mathematical operator.
print("shiva"+"sai")
print("shiva"*2)

#len()
c="shivasai"
print(len(c))

#membership operator

s="shiva"
print('s' in s)
print('f' not in s)
print('i' not in s)

#Removing spaces from strings.

txt = "      banana      "
txt1 = "     cherry      "
txt2 = "     Apple       "
x=txt.lstrip()
print("of all fruits",x,"is my fav.")
y=txt1.rstrip()
print("of all fruits",y,"is my fav.")
z=txt2.strip()
print("of all fruits",z,"is my fav.")

#substrings:
"""Retruns index of 1st occurence of the given substring.
if it is not available then we will get -1"""
s = "Learning python is very easy!!"
print(s.find('python'))
print(s.find('java'))
print(s.find('r'))
print(s.rfind('r'))


#count substring
"""no.of occurrences of substring present in the given string by using count() method."""
r="abaabaababbaababbabbabbab"
print(r.count('b'))
print(r.count('a'))

#Replacing a string with another string.
d = "Learning python was very simple."
print(d.replace("simple", "easy"))



#joining of strings.
"""we can join a group of strings(list or tuple) wrt the given seperator"""
t=("list","set","Dict")
print('-'.join(t))

#splitting of strings:
b = "Teks Academy Ameerpet"
l = b.split()
print(l)


day = "22-07-2001"
date = day.split('-')
for g in date:
    print(g)


#changing cases of a string:
h = "HyderABad..!12"
print(h.upper())
print(h.lower())
print(h.swapcase())
print(h.title())
print(h.capitalize())


#check type of characters present in a string.
jk = "nageshdeva127@gmail.com"
print(jk.isalpha())
print(jk.isalnum())
print(jk.isdigit())
print(jk.islower())
print(jk.isupper())
print(jk.istitle())
print(jk.isspace())


#checking starting and ending part of a string.
gv = "Learn python in a simple way."
print(gv.startswith('Learn'))
print(gv.endswith('simple'))



#formatting the strings.
name ="nagesh"
salary = 15000
age = 23
print("{}'s salary is {} and his age is {}".format(name,salary,age))
print("{0}'s salary is {1} and his age is {2}".format(name,salary,age))
print("{x}'s salary is {y} and his age is {z}".format(x="name",y="salary",z="age"))
print(f"{name}'s salary is {salary} and his age is {age}")

