def add(x, y=3):
    total = x + y
    return total


# Named arguments
print(add(x=5, y=2))

# This will give an error since all subsequent arguments should also have a name
# print(add(x=5, 2))
# No default value for x so error
# print (add(y=2))

# Output  1 - 2 - 3 - 4 - 5
print(1, 2, 3, 4, 5, sep=" - ")
