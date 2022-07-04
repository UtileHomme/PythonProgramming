colors = ['red', 'green', 'blue', 'orange']

# extract data
print(colors[1:3])

# assign data for mutable sequences
colors[1:3] = ['pink', 'black']
print(colors)

topic = 'Python Slicing'

# Extract data
print(topic[0:6])

# But we cannot assign data to immutable sequences
# topic[0:6] = 'Java'

# We can also use the slice object to get the indices

colors = ['red', 'green', 'blue', 'orange']
s = slice(1, 3)
print(s)
print(colors[s])

colors = ['red', 'green', 'blue', 'orange']

print(colors[-4:-2])

colors = ['red', 'green', 'blue', 'orange']
print(colors[-2:4])

colors = ['red', 'green', 'blue', 'orange']
print(colors[0:4:2])


# The indices method

# A slice object essentially defines a sequence of indices for selecting elements of a sequence.

# To make it more convenient, the slice type has the indices method that returns the equivalent range (start, stop, step) for any slice of a sequence with a specified length:

colors = ['red', 'green', 'blue', 'orange']

s = slice(0, 4, 2)
t = s.indices(len(colors))

for index in range(*t):
    print(colors[index])


