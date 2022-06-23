colors = ['red', 'blue', 'green']

red, blue, green = colors

print(red, blue, green)

# You have to have equal number of variables as the number of elements in the list
# To avoid the error, define as below. Others is another list now instead of a variable
red1, blue1, *others = colors

print(red1, blue1, others)