# LEGB
# Local, Enclosing, Global, Built In

# How does enclosing scope work

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

