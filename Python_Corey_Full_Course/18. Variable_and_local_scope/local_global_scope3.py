# LEGB
# Local, Enclosing, Global, Built In

# This is a global variable
x = 'global x'


def test(z):
    # When global is defined explicity, it means now the global x value is to be used and it can be modified
    global x
    y = 'local y'
    x = 'local X'

    print(x)

    print(z)

    print(y)

    # x is present in local scope, so inside the test function it will consider local x
    print(x)


test('local z')
print(x)

# Below code will not work, since y is not present in local, global or enclosing scope
# print(y)
