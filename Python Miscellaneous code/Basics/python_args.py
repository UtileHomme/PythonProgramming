x, y, *z = 10, 20, 30, 40

# z is unpacked as a list
print(x, y, z)


# Unpacking in a function

def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total


result = add(10, 20, 30, 40)
print(result)


# Printing arguments in *args

def add1(*args):
    print(args)


add1(1, 2, 3)


def add2(*args):
    print(args[0])
    print(args[1])
    print(args[2])


add2(1, 2, 3)


# After *args is set as a argument, no other variable can be defined after it except a keyword argument

# Below is not allowed

# def add(x, y, *args, z):
#     return x + y + sum(args) + z
#
# # For this z has no value because all are taken by the variable args
# add(10, 20, 30, 40, 50)

# Below is allowed
def add(x, y, *args, z):
    return x + y + sum(args) + z


add(10, 20, 30, 40, z=50)


# Unpacking a tuple

def point(x, y):
    return f'({x}, {y})'


a = (0, 0)

origin = point(*a)

print(origin)
