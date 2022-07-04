point = (100,200)

x = point[0]
y = point[1]

print(x,y)

# We can also do the above using class

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point2D):
            return self.x == other.x and self.y == other.y
        return False

# The __eq__ method checks if a point is an instance of the Point2D class and returns True if both x-coordinate and y-coordinate are equal.

a = Point2D(100, 200)
b = Point2D(100, 200)

print(a is b)  # False
print(a == b)  # true

# A better way to do the above is named tuples

# Named tuples allow you to create tuples and assign meaningful names to the positions of the tuple’s elements.
#
# Technically, a named tuple is a subclass of tuple. On top of that, it adds property names to the positional elements.

# To create a named tuple class, you need to the namedtuple function of the collections standard library.
#
# The namedtuple is a function that returns a new named tuple class. In other words, the namedtuple() is a class factory.
#
# To use the namedtuple function, you need to import it from the collections module first:

# The namedtuple function accepts the following arguments to generate a class:
#
# A class name that specifies the name of the named tuple class.
# A sequence of field names that correspond to the elements of tuples. The field names must be valid variable names except that they cannot start with an underscore (_).

from collections import namedtuple

Point2D = namedtuple('Point2D',['x','y'])

point = Point2D(100, 200)

print(isinstance(point, Point2D))  # True
print(isinstance(point, tuple))  # True

# Accessing data of a named tuple

# unpacking
x, y = point
print(f'({x}, {y})')  # (100, 200)

# indexing
x = point[0]
y = point[1]
print(f'({x}, {y})')  # (100, 200)

# iterating

for coordinate in point:
    print(coordinate)

#Renaming invalid field names

# The namedtuple function accepts the rename the keyword-only argument that allows you to rename invalid field names.
#
# The following results in an error because the field name _radius starts with an underscore (_):

from collections import namedtuple

# Circle = namedtuple(
#     'Circle',
#     'center_x, center_y, _radius'
# )

# The above will give the below error
#
# raise ValueError('Field names cannot start with an underscore: '
# ValueError: Field names cannot start with an underscore: '_radius'

# To resolve the above
from collections import namedtuple

Circle = namedtuple(
    'Circle',
    'center_x, center_y, _radius',
    rename=True
)

print(Circle._fields)

# Additional Python functions of named tuples
# Named tuples provide some useful functions out of the box. For example, you can use the equal operator (==) to compare two named tuple instances:

a = Point2D(100, 200)
b = Point2D(100, 200)

print(a == b)  # True

# If you use the class, you need to implement the __eq__ to get this function.

# Also, you can get the string representation of a named tuple:

print(a)
#
# Output:
#
# Point2D(x=100, y=200)
#
# Again, if you use the class, you need to implement __rep__ method.
#
# Since a named tuple is a tuple, you can apply any function that is relevant to a regular tuple to a named tuple. For example:

print(max(a))  # 200
print(min(a))  # 100