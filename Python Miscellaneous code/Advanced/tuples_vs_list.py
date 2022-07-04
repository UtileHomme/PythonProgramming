# 1. A tuple is immutable while a list is mutable

# List
fruits = ['apple', 'orange', 'banana']
fruits[0] = 'strawberry'

print(fruits)

# Tuple
fruits1 = ('apple', 'orange', 'banana')

# Below statement will give error
# fruits1[0] = 'strawberry'

# But we can do below
fruits1 = ('strawberry', 'orange', 'banana')
print(fruits1)

# 2. The storage efficiency of a tuple is greater than a list

from sys import getsizeof

fruits = ['apple', 'orange', 'banana']
print(f'The size of the list is {getsizeof(fruits)} bytes.')

fruits = ('strawberry', 'orange', 'banana')
print(f'The size of the tuple is {getsizeof(fruits)} bytes.')

# 3. Copying a tuple is faster than a list

# When you copy a list, Python creates a new list. The following example illustrates copying a list to another:

fruit_list = ['apple', 'orange', 'banana']
fruit_list2 = list(fruit_list)
print(id(fruit_list) == id(fruit_list2))  # False

# However, when copying a tuple, Python just reuses an existing tuple. It doesn’t create a new tuple because tuples are immutable.

fruit_tuple = ('apple', 'orange', 'banana')
fruit_tuple2 = tuple(fruit_tuple)
print(id(fruit_tuple) == id(fruit_tuple2))  # True

