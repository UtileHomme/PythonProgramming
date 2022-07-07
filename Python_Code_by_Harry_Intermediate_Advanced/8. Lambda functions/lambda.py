'''
Syntax:
lambda argument: manipulate(argument)
'''


def add(a, b):
    s = a + b
    return s


print(add(2, 3))

add1 = lambda a, b: a + b

print(add1(2, 4))

# List of tuples
a = [(1,2), (4,5), (555,34)]

a.sort(key=lambda x:x[1])

print(a)


