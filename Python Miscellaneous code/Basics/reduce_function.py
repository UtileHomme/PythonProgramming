from functools import reduce

scores = [1, 2, 3, 4, 5]

total = 0

for score in scores:
    total += score

print(total)

# Using reduce to reduce the list to a single value

total1 = 0


def sum(a, b):
    return a + b


total1 = reduce(sum, scores)

print(total1)

# Using lambda function

total2 = reduce(lambda a,b :a+b, scores)

print(total2)
