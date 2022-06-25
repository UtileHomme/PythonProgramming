# Read file content using read
with open('readme1.txt') as f:
    contents = f.read()
    print(contents)

# Read file content using readlines
# This will return a list of strings

lines = []
with open('readme2.txt') as f:
    lines = f.readlines()

for line in lines:
    print(line)

print("\n")

# Read file content using readline
# This will return all lines as strings

with open('readme2.txt') as f:
    lined = f.readline()

    while lined:
        lined = f.readline()
        print(lined)

# Another way

with open('readme3.txt') as f:
    for line in f:
        print(line)

# How to open files which have non-ascii characters

with open('readme.txt', encoding= 'utf-8') as f:
    for line in f:
        print(line)

