dict={1:'navaneeth', 2:'Nagesh', 3:'shiva', 4:'Naveen', 5:True, 6: 6}
print(dict) 
dict[5]='3'
print(dict)
dict[19]='charan'
print(dict)
for k in dict.keys():
    print(k)
for v in dict.values():
    print(v)
for k,v in dict.items():
    print(k,'--------',v)
print(len(dict))

"""fromkeys(): creates a new dicitionary with keys from a sequence and values
set to a defalut value."""
keys=['a','b','c']
default_value=0
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

"""get(): Returns the value associated with a key, or a default value if the key is not present"""
my_dict = {'a':1, 'b': 2, 'c': 3}
value = my_dict.get('b')
print(value)
"""items(): Returns a view object that displays a list of a dictionary's key-value pairs."""
myy_dict = {'a': 1, 'b': 2, 'c': 3}
value=myy_dict.items()
print(value)
"""keys(): Returns a view object that displays a list of the dictionary's keys."""
my_dictt = {'a': 1, 'b': 2, 'c': 3}
keyss = my_dictt.keys()
print(keyss)
"""values(): Returns a view object that displays a list of the dictionary's values."""
my_dicct = {'a': 1, 'b': 2, 'c': 3}
valuess = my_dicct.values()
print(valuess)
"""pop(): Removes and returns the value associated with a specified key."""
dictt = {'a':'nagesh', 'b': 'deva', 'c': 'shiva', 'd': 'naveen'}
A = dictt.pop('c')
print(A)
"""popitem(): Removes and returns the last inserted key-value pair as a tuple"""
dictionary = {'a':'nagesh', 'b': 'deva', 'c': 'shiva', 'd': 'naveen', 'd': 'charan'}
item_pop = dictionary.popitem()
print(item_pop)
"""update(): Updates the dictionary with the key-value pairs from another dictionary or iterable."""
dictionaryy = {'a':'nagesh', 'b': 'deva', 'c': 'shiva', 'd': 'naveen', 'd': 'charan'}
other_dict = {1: 'Teks Academy', 2: 'Ameerpet'} 
dictionaryy.update(other_dict)
print(dictionaryy)



#Merging Dictionaries:
"""Write a Python function that takes two dictionaries as input and
 returns a new dictionary that contains all the key-value pairs from both 
 dictionaries. If there are common keys, the values from the second dictionary should be used."""
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dictionaries(dict1, dict2))


#inverse Dictionary
"""Write a Python function that takes a dictionary as input and returns
 a new dictionary where the keys and values are swapped."""
def inverse_dictionary(input_dict):
    inverse_dict = {value: key for key, value in input_dict.items()}
    return inverse_dict

input_dict = {'a': 1, 'b': 2, 'c': 3}
print(inverse_dictionary(input_dict))


#set comprehensions
squares = {x:x*x for x in range(1,6)}
print(squares)
doubles= {x:2*x for x in range(1,6)}
print(doubles)