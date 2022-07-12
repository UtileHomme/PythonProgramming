# LEGB
# Local, Enclosing, Global, Built In

# builtins are also the python variables or functions which are part of the python library
import builtins

print(dir(builtins))

# This function is overriding the built in min function which calculates the builtin function
def min(*args):
    return 'hello'

m = min([5, 1, 2, 3, 4])
print(m)
