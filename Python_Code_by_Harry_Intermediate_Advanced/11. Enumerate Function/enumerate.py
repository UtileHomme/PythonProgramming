a = ['a', 'b', 'c', 'd']

# How to print index and value in a list
for i, item in enumerate(a):
    print(i, item)

# Print the values whose indexes are a multiple of 2
for i, item in enumerate(a):
    if (i + 1) % 2 == 0:
        print(item)
