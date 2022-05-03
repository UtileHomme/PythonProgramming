import sys

file = open('data.txt', 'r')

# This gives a list
lines = file.readlines()

file.close()

print(lines)

# We want to skip the first row in the csv which is the headers
# Used for removing the first element of the list
lines = [line.strip() for line in lines[1:]]

for line in lines:
    # This will give the first line split by comma
    person_data = line.split(',')
    name = person_data[0].title()  # Title turns string into camelcase
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}.')

# How to create a csv file using , as the delimiter
sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)
