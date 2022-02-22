friends = ["Rolf", "John", "Anna"]

counter = 0

# enumerate is used to join the above list with a number
'''
OUTPUT
Rolf
1
John
2
Anna
'''
for counter,friend in enumerate(friends):
    print(counter)
    print(friend)

# [(0, 'Rolf'), (1, 'John'), (2, 'Anna')]
print(list(enumerate(friends)))

# {0: 'Rolf', 1: 'John', 2: 'Anna'}
print(dict(enumerate(friends)))

# {1: 'Rolf', 2: 'John', 3: 'Anna'} - to start with index 1
print(dict(enumerate(friends, 1)))