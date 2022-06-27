a = 10
b = 3

print(a//b)  # 3

a = -10
b = -3

print(a//b)  # 3

a = 10
b = -3
print(a//b)  # -4

a = -10
b = 3
print(a//b)  # -4

# The same thing can be done using the math floor function

from math import floor

a = 10
b = -3

print(a//b)  # -4
print(floor(a/b))  # -4
