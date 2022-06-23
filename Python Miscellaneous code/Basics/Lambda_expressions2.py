# 1. Function that return a function

def times(n):
    return lambda x: x * n


# double is also a function
double = times(2)

print(double(2))

# 2. Python Lambda in a loop

callables = []

for i in (1, 2, 3):
    callables.append(lambda a=i: a)

for f in callables:
    print(f())
