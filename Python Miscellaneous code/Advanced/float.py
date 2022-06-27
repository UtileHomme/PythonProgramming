x = 0.1 + 0.1 + 0.1
y = 0.3

# False
print(x == y)

# As you can see below, the two numbers are different
print(format(x, '.20f'))
print(format(y, '.20f'))

# One way to solve the problem

x = 0.1 + 0.1 + 0.1
y = 0.3
print(round(x, 3) == round(y, 3))

# Second way to solve the problem

from math import isclose

x = 0.1 + 0.1 + 0.1
y = 0.3

print(isclose(x,y))
