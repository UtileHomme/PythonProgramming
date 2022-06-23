colors = ['red', 'green', 'blue']

# Iterables are elements that can be iterated over e.g. List, tuples, strings etc.

# Iterators are elements that facilitate the iteration
colors_iter = iter(colors)

color = next(colors_iter)

print(color)


color = next(colors_iter)

print(color)


color = next(colors_iter)

print(color)

# This will give an exception, since no more elements exist
# color = next(colors_iter)
#
# print(color)

# Once an iterator has finished its job, it no longer has any value

colors = ['red1', 'green2', 'blue3']

iterator = iter(colors)

for color in iterator:
    print(color)