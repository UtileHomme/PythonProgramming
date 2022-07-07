'''

Iterable - An object in which __iter__ and __getitem__ is defined and which can be iterated over. This can give us an iterator
Iterator - An object in which __next__ method is defined. Using next, we can go to next element
Iteration -

'''


# Generators will not print the result but will generate it into the memory

# for i in range(500):
#     print(i)

def gen(n):
    for i in range(n):
        yield i


# This gives an iterator
genIterator = gen(100)
# for i in genIterator:
#     print(i)

print(next(genIterator))
print(next(genIterator))

# Integer is not iterable
num = 345

# for i in num:
#     print i

# String is iterable
num1 = "jatin"

for i in num1:
    print(i)

#     Creating an iterable
iter1 = iter(num1)

print(next(iter1))
print(next(iter1))

