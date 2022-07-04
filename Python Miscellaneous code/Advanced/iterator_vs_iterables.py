# Iterators
# An iterator is an object that implements the iterator protocol. In other words, an iterator is an object that implements the following methods:

# __iter__ returns the iterator object itself.
# __next__ returns the next element.
# Once you complete iterating a collection using an iterator, the iterator becomes exhausted.

# It means that you cannot use the iterator object again.

# Iterables
# An iterable is an object that you can iterate over.

# An object is iterable when it implements the __iter__ method. And its __iter__ method returns a new iterator.

# Examining the built-in-list and list iterator

numbers = [1, 2, 3]

# This is an iterator
number_iterator = numbers.__iter__()
print(type(number_iterator))

# In this example, the __iter__ method returns an iterator with the type list_iterator.

# Because the list_iterator implements the __iter__ method, you can use the iter built-in function to get the iterator object:

numbers = [1, 2, 3]
number_iterator = iter(numbers)

# Since the list_iterator also implements the __next__ method, you can use the built-in function next to iterate over the list:

numbers = [1, 2, 3]

number_iterator = iter(numbers)

next(number_iterator)
next(number_iterator)
next(number_iterator)


# Example for Iterator and iterable

class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.rgb):
            raise StopIteration

        # return the next color
        color = self.rgb[self.__index]
        self.__index += 1
        return color


# In this example, the Colors class plays two roles: iterable and iterator.
#
# The Colors class is an iterator because it implements both __iter__ and __next__ method. The __iter__ method returns the object itself. And the __next__ method returns the next item from a list.
#
# The Colors class is also an iterable because it implements the __iter__ method that returns an object itself, which is an iterator.

colors = Colors()

for color in colors:
    print(color)


# Separating an iterator from an iterable

class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)


class ColorIterator:
    def __init__(self, colors):
        self.__colors = colors
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__colors):
            raise StopIteration

        # return the next color
        color = self.__colors.rgb[self.__index]
        self.__index += 1
        return color

colors = Colors()
color_iterator = ColorIterator(colors)

for color in color_iterator:
    print(color)

# How it works.
#
# The __init__ method accepts an iterable which is an instance of the Colors class.
# The __iter__ method returns the iterator itself.
# The __next__ method returns the next element from the Colors object.

# To iterate the Colors object again, you just need to create a new instance of the ColorIterator.
#
# There’s one problem!
#
# When you want to iterate the Colors object, you need to manually create a new ColorIterator object. And you also need to remember the iterator name ColorIterator.
#
# It would be great if you can automate this. To do it, you can make the Colors class iterable by implementing the __iter__ method:

class Colors:
    def __init__(self):
        self.rgb = ['red', 'green', 'blue']

    def __len__(self):
        return len(self.rgb)

    # Now we don't need to define a new colorIterator object
    def __iter__(self):
        return self.ColorIterator(self)

    class ColorIterator:
        def __init__(self, colors):
            self.__colors = colors
            self.__index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.__index >= len(self.__colors):
                raise StopIteration

            # return the next color
            color = self.__colors.rgb[self.__index]
            self.__index += 1
            return color

colors = Colors()

for color in colors:
    print(color)

