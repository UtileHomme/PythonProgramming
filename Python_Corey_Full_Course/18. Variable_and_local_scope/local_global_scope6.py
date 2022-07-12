# LEGB
# Local, Enclosing, Global, Built In

# How does enclosing scope work

def outer():
    x = 'outer x'

    def inner():
        # This will now affect the outer x variable
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    # The value of outer x is also set via the inner function
    print(x)

outer()

