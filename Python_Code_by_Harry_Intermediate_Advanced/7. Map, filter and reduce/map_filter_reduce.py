# Map function
#  map(function_to_apply, list of inputs)

list1 = [1,2,3,5,6]
sq = []
# We want to make another list which is a square of all elements in the list

for item in list1:
    sq.append(item**2)

print(sq)

# Using map
def square(n):
    return n**2

sq1 = []

# sq1 is a map object
sq1 = map(square, list1)
sqList = list(sq1)

print(sqList)




