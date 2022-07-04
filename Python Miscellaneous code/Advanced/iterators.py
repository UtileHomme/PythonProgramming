# An iterator is an object that implements:
#
# __iter__ method that returns the object itself.
# __next__ method that returns the next item. If all the items have been returned, the method raises a StopIteration exception.
# Note that these two methods are also known as the iterator protocol.
#
# Python allows you to use iterators in for loops, comprehensions, and other built-in functions including map, filter, reduce, and zip.

class Square:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.length:
            raise StopIteration

        self.current += 1
        return self.current ** 2

square = Square(5)

for sq in square:
    print(sq)