import prime
import prime as pr # imports all functions in the file
from prime import primeTo  # imports only the particular function

primeTo(100)

import prime

print(dir(prime))  # dir(module) dir takes the module as param returns all the functions

import main.sub2.prime as sub2  # accessing the sub modules

sub2.primeTo(10)

from main.sub2.prime import primeTo

primeTo(20)


# Built in Modules

import copy

my_dictionary = { "key": "value", ("k", "e", "y"): 5 }
my_dictionary1 = copy.deepcopy(my_dictionary)
my_dictionary[1] = 1
print(my_dictionary) # {'key': 'value', ('k', 'e', 'y'): 5, 1: 1}
print(my_dictionary1) # {'key': 'value', ('k', 'e', 'y'): 5}

import math as m   # used for nomal numbers

print(m.exp(1)) # 2.718281828459045
print(m.cos(m.pi)) # -1.0
print(m.ceil(1.4)) # 2
print(m.floor(1.4)) # 1

import cmath as cm  # used for complex numbers (numbers with imaginary values)

print(cm.sqrt(4)) # (2+0j)

print(cm.polar(complex())) # (0.0, 0.0)

print(cm.polar(complex(1, 3))) # (3.1622776601683795, 1.2490457723982544)

import random as ran

print(ran.sample([1, 2, 3, 4, 5], 3)) # [4, 1, 5]  [5, 1, 4]  [3, 1, 4] ... 
print(ran.random()) # prints random numbers between 0 to 1
print(ran.randint(5, 100))  # prints random numbers between 5 to 100 int values

import sys

print(sys.getrecursionlimit()) # 1000
print(sys.version) # 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)]
print(sys.path) # return all python packages file paths