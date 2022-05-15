friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# Stores the ID of the data in the memory
# 2181926463168
print(id(friends_last_seen))

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

# Stores the ID of the data in the memory
# This ID will be different from the last

# 2181926463240
print(id(friends_last_seen))

friends_last_seen['Rolf'] = 0

# The last ID in the previous iteration is changed to 0
# 2181926463240
print(id(friends_last_seen))

# Ints, floats, tuples, strings are always immutable
my_int = 5

# 1762225344
print(id(my_int))

my_int = my_int + 1

# 1762225376
print(id(my_int))

# Lists are mutable
friends = ['Rolf', 'Jose']

# 2181929694088
print(id(friends))

friends.append('Jen')

# 2181929694088
print(id(friends))




