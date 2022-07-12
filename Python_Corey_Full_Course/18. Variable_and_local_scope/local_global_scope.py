# LEGB
# Local, Enclosing, Global, Built In

# This is a global variable
x = 'global x'


def test():
    y = 'local y'

    print(y)

    # x is not present in local scope, but x is present in enclosing scope
    print(x)

    # x = 'local X'

    print(x)


test()

# Below code will not work, since y is not present in local, global or enclosing scope
# print(y)
