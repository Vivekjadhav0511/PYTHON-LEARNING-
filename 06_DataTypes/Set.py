
# Set In Python a set is an unordered collection of unique elements. I

""" Key Feacture => 
    Unordered: The elements do not have a specific order.
    Unique: Duplicate elements are not allowed.
    Mutable: You can add or remove elements.  """

setOne = {1,2,3}

print(setOne & {1,3}) # In Python, the & operator can be used directly with sets to perform a set intersection, which returns the common elements between two sets.

print (setOne | {4, 8, 777})  # In Python, the | operator is used with sets to perform a union operation. This combines all unique elements from two sets into a new set.

print(set("vivek"))

print(({1,2,3544,1,2}))