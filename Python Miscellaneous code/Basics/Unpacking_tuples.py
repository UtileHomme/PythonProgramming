# Below will give error in unpacking because there are two variables on the left and three on the right
# x, y = (10, 20, 30)

# Below is the solution
x, y, _ = (10, 20, 30)

print(x, y, _)

x, y, *z = (10, 20, 45, 50)

# z will be a list of elements
print(x, y, z)
