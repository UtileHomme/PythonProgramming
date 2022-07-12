# LEGB
# Local, Enclosing, Global, Built In

# How does enclosing scope work
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        # This will use the x value in the enclosing scope
        print(x)

    inner()
    # The value of outer x is also set via the inner function
    print(x)

outer()
print(x)

