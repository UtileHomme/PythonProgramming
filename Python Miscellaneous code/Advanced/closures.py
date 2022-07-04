def say():
    greeting = 'Hello'

    def display():
        print(greeting)

    display()

# a closure is a nested function that references one or more variables from its enclosing scope.
# The  combination of display function and greeting variable is a closure

# How to return an inner function

def say():
    greeting = 'Hello'

    def display():
        print(greeting)

    return display

# The following assigns the return value of the say function to a variable fn. Since fn is a function, you can execute it:

fn = say()
fn()

# When does Python create closures

# Python creates a new scope when a function executes. If that function creates a closure, Python also creates a new closure as well.

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

# m1, m2, m3 are functions now
m1 = multiplier(1)
m2 = multiplier(2)
m3 = multiplier(3)

print(m1(10))
print(m2(10))
print(m3(10))

# How to do above using a for loop

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


multipliers = []
for x in range(1, 4):
    multipliers.append(multiplier(x))

print(multipliers)
m1, m2, m3 = multipliers

print(m1(10))
print(m2(10))
print(m3(10))

