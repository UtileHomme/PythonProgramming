# Reduce function
#  makes a list of elements for which a function returns True

from functools import reduce

def sum_num(a,b):
    return a+b

# First 1 and 2 will be added which gives three
# Then 3 and 3 will be added which gives 6
# Then 6 and 4 will be added to get 10
list1 = reduce(sum_num, [1,2,3,4])

print(list1)