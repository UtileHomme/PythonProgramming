# 1. Basic Slicing example

colors = ['red', 'orange', 'yellow', 'green', 'blue']

sub_colors = colors[1:4]

print(sub_colors)

# 2. How to get n first elements from list

n_first_elements = colors[:5]

print(n_first_elements)

# 3. How to get n last elements

n_last_elements = colors[-3:]

print(n_last_elements)

# 4. How to get nth element from the list

# iterate in steps of 2
nth_element = colors[::2]

print(nth_element)

# 5. How to reverse a list

reversed_colors = colors[::-1]

print(reversed_colors)

# 6. Substitute part of a list

colors[0:2] = ['black', 'white']

print(colors)

# 7. Partially replace and resize a list

colors[0:2] = ['magenta', 'cyan', 'grey']

print(colors)

# Deleting elements from a list

del colors[2:5]