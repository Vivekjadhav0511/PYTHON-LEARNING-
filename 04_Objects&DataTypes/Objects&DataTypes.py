# Objects And DataTypes in Python 

""" Mutable 
Values can be modified => Examples: list, dict, set

Immutable
Values cannot be modified => Examples: int, str, tuple """

Numbers = 1234

String = "Vivek Jadhav"

myList = [10,20,40,60,] 
print(myList)

tuples = (2,"spam",6,6,99,35)

dictionary = {  
    'name':'Vivek',
    'age': 41
}  
#   key value pair => dict

set = set('abc')

# file = open('myFile.txt')

boolean = True

# None = None 

# functions , modules , classes 

# ADVANCE => decorater , Generator , itarator 

import math

print(math.pi)

username = "vivekjadhav"
print(len(username))
print(username[1]) 
# string does not Support item assignment 

dir(username)

# ______________________________

list = [125, "vivek", 414]

print(len(list),list[0])

dict = {
    'username' : "mike@456",
    'age' : 77
}

print(dict, dict['username'])

tuple = (777,411,44,744)
print(tuple, tuple[0], len(tuple))

# *************

# Copy & DeepCopy

l1 = [1,2,3]
l2 = l1
print(l1)
print(l2)

""" Change In Referance  """

l1 = "Vivek"     
print(l1)
print(l2)
print(l1 == l2)

import copy
h2 = copy.copy(l1)
print("importCopy", h2)

list4 = [1,2,1,5,[4,5,5,[541,888]]]
list5 = copy.copy(list4)
list6 = list4 [:]
print(list5)
print(list6)


