'''

List comprehensions
Dictionary comprehenesions
Set Comprehensions
Generator Comprehensions
'''

# LIST COMPREHENSIONS
list1 = [1, 32, 4, 5, 45, 6, 9, 343]

divide_by_3 = []

print("Without using list comprehensions")

for item in list1:
    if item % 3 == 0:
        divide_by_3.append(item)

print(divide_by_3)

print("Using list comprehensions")

divide_by_3 = [item for item in list1 if item % 3 == 0]

print(divide_by_3)

# DICTIONARY COMPREHENSIONS

dict1 = {
    'a': 45,
    'A': 5,
    'b': 65
}

dict2 = {}

for k in dict1.keys():
    if k.lower() in dict1.keys():
        dict2[k] = dict1.get(k)
    if k.upper() in dict1.keys():
        dict2[k] = dict1.get(k)

print(dict2)

# It will add k.lower and it's corresponding value using the get(), It will also check for the uppercase version and add it too to the dictionary
# second argument of get() is the default value in case key is not found
# simulation of above for loop.
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

# SET COMPREHENSIONS

# Sets will have unique values in the end
squares = {x ** 2 for x in [1, 2, 3, 4, 4, 4, 4, 5, 5, 6, 6]}

print(squares)

# GENERATOR COMPREHENSIONS

# gen is a iterator object
gen = (i for i in range(56) if i % 3 == 0)

for item in gen:
    print(item)
