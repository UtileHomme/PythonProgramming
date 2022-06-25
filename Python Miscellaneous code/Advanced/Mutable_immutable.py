# Immutablles

'''
Numbers
Strings
Tuples
Frozen Sets
'''

# Mutables

'''
Lists
Sets
Dictionaries
'''

# Example for numbers (immutable)
counter = 100

print(id(counter))

counter = 200

print(id(counter))

# Example for lists (mutable)

ratings = [1,2,3]

print(id(ratings))

ratings.append(4)

print(id(ratings))
