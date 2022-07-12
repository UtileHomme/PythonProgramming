# LEGB
# Local, Enclosing, Global, Built In

# This is a global variable
x = 'global x'


def test():
    y = 'local y'
    x = 'local X'

    print(y)

    # x is present in local scope, so inside the test function it will consider local x
    print(x)


test()
print(x)

# Below code will not work, since y is not present in local, global or enclosing scope
# print(y)
