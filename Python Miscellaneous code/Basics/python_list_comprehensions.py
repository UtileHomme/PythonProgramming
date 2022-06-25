numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# Another way of doing the same thing using maps

squares1 = list(map(lambda number: number * 2, numbers))

print(squares1)

# Another way of doing the same thing using list comprehensions

squares2 = [number ** 2 for number in numbers]

print(squares2)

# Using list comprehensions with if condition

mountains = [
    ['Makalu', 8785],
    ['Lhotse', 8716],
    ['Kanchengunga', 8586]
]

highest_mountains = [m for m in mountains if m[1] > 8600]

print(highest_mountains)
