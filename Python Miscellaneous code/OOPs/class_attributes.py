class Circle:
    def __init__(self, radius):
        # These are instance attributes
        self.pi = 3.14159
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2*self.pi * self.radius

# We can also define class Attributes which will not belong to a specific instance of the class
# They are shared by all instances of the class

class Circle:
    # this is a CLASS attribute
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius

# Way to access class Attributes
c = Circle(10)
print(c.pi)
print(Circle.pi)

# Difference between class and instance attributes

class Test:
    x = 10

    def __init__(self):
        self.x = 20


test = Test()
print(test.x)  # 20
print(Test.x)  # 10

# Examples of usage of Class attributes

# 1. For tracking data across all instances

class Circle:
    circle_list = []
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
        # add the instance to the circle list
        self.circle_list.append(radius)

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2 * self.pi * self.radius


c1 = Circle(10)
c2 = Circle(20)

print(len(Circle.circle_list))  # 2
print(c1.circle_list)
print(c2.circle_list)

# 2. For defining default values

class Product:
    default_discount = 0

    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)


p1 = Product(100)
print(p1.net_price())
 # 100

p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())
 # 190




