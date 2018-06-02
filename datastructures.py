# Data Structures:
# 1. tuples - sequence of immutable objects

tup = (1, "abc", 2, "def")
tup1 = 3, "ghi", True

tup2 = "A"

print(tup) # (1, 'abc', 2, 'def')
print(tup[0]) # 1
print(tup[0:2]) # (1, 'abc') # slice

try:
    tup[3] = 5
except Exception as e:
    print(e)  # 'tuple' object does not support item assignment

tup = tup[0:3] + (5,)
print(tup) # (1, 'abc', 2, 5)
print(tup1 * 2) # (3, 'ghi', True, 3, 'ghi', True)
print(5 in tup) # True
for x in tup:
    print(x)

def multiple_result():
    return(1, 2, 3)

print(multiple_result()) # (1, 2, 3)
print((1, 2, 3) == (1, 2)) # False

# functions with tuple

tup3 = (1, 2, 5, 7)
print(len(tup3)) # 4
print(max(tup3)) # 7
print(min(tup3)) # 1

list1 = [1, "abc", (2, 3)]
list2 = list1 + [4]
print(list2) # [1, 'abc', (2, 3), 4]
print(list1[2]) # (2, 3)
print(list1[2][0]) # 2
print(list1 * 3) # [1, 'abc', (2, 3), 1, 'abc', (2, 3), 1, 'abc', (2, 3)]
print(2 in list1) # False
print(2 in list1[2]) # True
print(list1 == [1, "abc", (2, 3)]) # True
print(list1[:2]) # slice # [1, 'abc']
list1.append(6) # [1, 'abc', (2, 3), 6]
list1[len(list1):] = [7] # [1, 'abc', (2, 3), 6, 7]
print(list1)

# List functions:
mapList = list(map(lambda x: x**2 + 3*x + 1, [1, 2, 3, 4]))
print(mapList) # [5, 11, 19, 29]

filteredList = list(filter(lambda x: x < 4, [1, 2, 3, 4, 5, 4, 3, 2, 1]))
print(filteredList) # [1, 2, 3, 3, 2, 1]

import functools
reducedList = functools.reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(reducedList) # 24

# Dictionaries: -- Object
my_dictionary = { "key": "value", ("k", "e", "y"): 5 }
my_dictionary1 = { x: x+1 for x in range(10) }

print(my_dictionary) # {'key': 'value', ('k', 'e', 'y'): 5}
print(my_dictionary1) # {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

try:
    print(my_dictionary[1])
except Exception as e:
    print(e)

print(my_dictionary.keys()) # dict_keys(['key', ('k', 'e', 'y')])
print(my_dictionary.values()) # dict_values(['value', 5])

my_dictionary[2] = 5
print(my_dictionary) # {'key': 'value', ('k', 'e', 'y'): 5, 2: 5}
del my_dictionary[2]
print(my_dictionary) # {'key': 'value', ('k', 'e', 'y'): 5}

my_dictionary.clear()
print(my_dictionary) # {}

# Shallow copies with Dictionaries:
# shallow copy = two copies of a data structure share the same set of elements

my_dictionary2 = { "item": "shirt", "size": "medium", "price": 50 }
my_dictionary3 = my_dictionary2

print(my_dictionary2) # {'item': 'shirt', 'size': 'medium', 'price': 50}
my_dictionary2["price"] = 100
print(my_dictionary3) # {'item': 'shirt', 'size': 'medium', 'price': 100}

mt_set = set(["one", "two", "three", "one"])
mt_set2 = set(["two", "three", "four"])
print(mt_set) # {'one', 'three', 'two'}
print(mt_set | mt_set2) # {'one', 'three', 'two', 'four'}
print(mt_set ^ mt_set2) # {'one', 'four'}
a = mt_set - mt_set2
print(mt_set - mt_set2) # {'one'}
print(a >= mt_set) # False
print(a <= mt_set) # True
mt_set.add("five")
print(mt_set) # {'one', 'two', 'three', 'five'}

# Set Functions:
print(set.union(mt_set, mt_set2)) # {'one', 'five', 'two', 'four', 'three'}
print(set.intersection(mt_set, mt_set2)) # {'three', 'two'}
print(set.difference(mt_set, mt_set2)) # {'five', 'one'}