# Typically, Python executes a regular function from top to bottom based on the run-to-completion model.
#
# It means that Python cannot pause a regular function midway and then resumes the function after that. For example:

def greeting():
    print('Hi!')
    print('How are you?')
    print('Are you there?')

# When Python executes the greeting() function, it executes the code line by line from top to bottom.
#
# Also, Python cannot pause the function at the following line:

print('How are you?')

# … and jumps to another code and resumes the execution from that line.
#
# To pause a function midway and resume from where the function was paused, you use the yield statement.
#
# When a function contains at least one yield statement, it’s a generator function.
#
# By definition, a generator is a function that contains at least one yield statement.
#
# When you call a generator function, it returns a new generator object. However, it doesn’t start the function.
#
# Generator objects (or generators) implement the iterator protocol. In fact, generators are lazy iterators. Therefore, to execute a generator function, you call the next() built-in function on it.

def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

# Messenger is now an iterator
messenger = greeting()

result = next(messenger)
print(result)

result = next(messenger)
print(result)

# Using Python generators to use iterators

# Old way of definining iterator

# class Squares:
#     def __init__(self, length):
#         self.length = length
#         self.current = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         result = self.current ** 2
#
#         self.current += 1
#
#         if self.current > self.length:
#             raise StopIteration
#
#         return result

# length = 5
# square = Squares(length)
# for s in square:
#     print(s)

# Definining Iterator using generators

def squares(length):
    for n in range(length):
        yield n ** 2

for s in squares(5):
    print(s)



