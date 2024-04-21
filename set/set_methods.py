s = {1,2,3,4,5}
print(s)
print(type(s))


#methods:
#clear:
set1 = {23,54,90,60}
set1.clear()
print(set1)

#copy()
set1 = {23,54,90,60,'nagesh'}
set3 = set1.copy()
print(set3)


"""add(): Adds an element to the set.\
    -->Adds only 1 item to the set."""

set5 = {1,2,3,4}
set5.add(8)
print(set5)


"""update(): To add multiple items to the set.
    --> Arguments are not individual elements and these are iterable objects like list, Range"""
s = {10,20,30}
l = {40,50,60,70,10}
s.update(l)
print(s)

ss = {10,20,30}
ll = {40,50,60,80}
ss.update(ll,range(10))
print(ss)

"""remove(): Removes the specified element from the set."""

sett = {1,2,3,4,6}
sett.remove(2)
print(sett)

"""pop(): Removes and returns any element from the set."""

my_set = {1,2,3,4,5,6,7}
my_set.pop()
print(my_set)
my_set.pop()
print(my_set)

"""discard(): it removes specified from the set 
    But the difference between remove() & discard() is:
    discard()--> if the specified element not present in set it will not give any error."""
seet = {10,30,60,90}
seet.discard(40)
print(seet)
seet.discard(60)
print(seet)   
"""    
seet.remove(40)          #remove
print(seet)""" 


"""union(): Returns a new set containing all the unique elements from both sets."""
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2)
print(union_set)

"""intersection(): Returns a new set containing the common elements between two sets."""
set1 = {33,66,99}
set2 = {66,77,55,33}
intersection_set = set1.intersection(set2)
print(intersection_set)

"""difference(): Returns a new set containing elements that are present in the first set but not in the second set."""
set1 = {23,54,90,60}
set2 = {66,23,54,33}
difference_set = set1.difference(set2)
print(difference_set)
difference_sett = set2.difference(set1)
print(difference_sett)

"""Write a Python function that takes a list as input and returns a new list with duplicates removed using sets."""
def remove_duplicates(input_list):
    return list(set(input_list))

my_list = [1,2,3,4,5,6,7,4,5,2,2,9,0]
print(remove_duplicates(my_list))

"""Check for Common Elements in Two Lists:

Write a Python function that takes two lists as input and returns True if they have at least one common element, False otherwise."""
def common_elements(list1, list2):
    return len(set(list1).intersection(list2)) > 0

list1 = [1,2,3]
list2 = [3,4,5]
print(common_elements(list1, list2))


#set comprehension
s = {x*x for x in range(5)}
print(s)

s= {2**x for x in range (2,10,2)}
print(s)