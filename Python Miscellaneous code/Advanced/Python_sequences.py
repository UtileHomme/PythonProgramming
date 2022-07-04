# Python has the following built-in sequence types: lists, bytearrays, strings, tuples, range, and bytes. Python classifies sequence types as mutable and immutable.

# 1. Counting elements in a sequence

cities = ['San Francisco', 'New York', 'Washington DC']

print(len(cities))

# 2. Checking if an item exists in a Python sequence

cities = ['San Francisco', 'New York', 'Washington DC']
print('New York' in cities)

cities = ['San Francisco', 'New York', 'Washington DC']
print('New York' not in cities)

# 3. Finding the index of an item in a Python sequence

numbers = [1, 4, 5, 3, 5, 7, 8, 5]

print(numbers.index(5))

# 4. To find the index of the first occurrence of an item at or after a specific index, you use the following form of the index method:

numbers = [1, 4, 5, 3, 5, 7, 8, 5]

# Searches for 5 after index 3 values
print(numbers.index(5, 3))

# The following form of the index method allows you to find the index of the first occurrence of an item at or after the index i and before index j:

numbers = [1, 4, 5, 3, 5, 7, 8, 5]
print(numbers.index(5, 3, 5))

# 5. Slicing a sequence

numbers = [1, 4, 5, 3, 5, 7, 8, 5]

# The end index is not taken into consideration
print(numbers[2:6])

# The extended slice allows you to get a slice from i to (but not including j) in steps of k
numbers = [1, 4, 5, 3, 5, 7, 8, 5]

# i:j:k
print(numbers[2:6:2])

# 6. Getting min and max items from a Python sequence

numbers = [1, 4, 5, 3, 5, 7, 8, 5]

print(min(numbers))  # 1
print(max(numbers))  # 8

# 7. Concatenating two Python sequences

east = ['New York', 'New Jersey']
west = ['San Diego', 'San Francisco']

cities = east + west
print(cities)

# 8. Repeating a python sequence

s = 'ha'
print(s*3)
