class Car:
    def go(self):
        print('Going')

class Flyable:
    def fly(self):
        print('Flying')

class FlyingCar(Flyable, Car):
    pass

# Since the FlyingCar inherits from Car and Flyable classes, it reuses the methods from those classes. It means you can call the go() and fly() methods on an instance of the FlyingCar class like this:

if __name__ == '__main__':
    fc = FlyingCar()
    fc.go()
    fc.fly()

# First, add the start() method to the Car, Flyable, and FlyingCar classes. In the start() method of the FlyingCar class, call the start() method of the super():

class Car:
    def start(self):
        print('Start the Car')

    def go(self):
        print('Going')


class Flyable:
    def start(self):
        print('Start the Flyable object')

    def fly(self):
        print('Flying')


class FlyingCar(Flyable, Car):
    def start(self):
        super().start()

# Second, create an instance of the FlyingCar class and call the start() method:

if __name__ == '__main__':
    car = FlyingCar()
    car.start()

# Output:

# Start the Flyable object

# As you can see clearly from the output, the super().start() calls the start() method of the Flyable class.
#
# The following shows the __mro__ of the FlyingCar class:

print(FlyingCar.__mro__)

# Output:
#
# (<class '__main__.FlyingCar'>, <class '__main__.Flyable'>, <class '__main__.Car'>, <class 'object'>)

# From left to right, you’ll see the FlyingCar, Flyable, Car, and object.
#
# Note that the Car and Flyable objects inherit from the object class implicitly. When you call the start() method from the FlyingCar‘s object, Python uses the __mro__ class search path.

# Since the Flyable class is next to the FlyingCar class, the super().start() calls the start() method of the FlyingCar class.
#
# If you flip the order of Flyable and Car classes in the list, the __mro__ will change accordingly. For example:

# Car, Flyable classes...


class FlyingCar(Car, Flyable):
    def start(self):
        super().start()


if __name__ == '__main__':
    car = FlyingCar()
    car.start()

    print(FlyingCar.__mro__)

# Output:

# Start the Car
# (<class '__main__.FlyingCar'>, <class '__main__.Car'>, <class '__main__.Flyable'>, <class 'object'>)

# In this example, the super().start() calls the start() method of the Car class instead, based on their orders in the method order resolution.


# MULTIPLE INHERITANCE AND SUPER

class Car:
    def __init__(self, door, wheel):
        self.door = door
        self.wheel = wheel

    def start(self):
        print('Start the Car')

    def go(self):
        print('Going')

class Flyable:
    def __init__(self, wing):
        self.wing = wing

    def start(self):
        print('Start the Flyable object')

    def fly(self):
        print('Flying')

class FlyingCar(Flyable, Car):
    def __init__(self, door, wheel, wing):
        super().__init__(wing=wing)
        self.door = door
        self.wheel = wheel

    def start(self):
        super().start()

# The __init__ of the Car and Flyable classes accept a different number of parameters. If the FlyingCar class inherits from the Car and Flyable classes, its __init__ method needs to call the right __init__ method specified in the method order resolution __mro__ of the FlyingCar class.

# The method order resolution of the FlyingCar class is:
# (<class '__main__.FlyingCar'>, <class '__main__.Flyable'>, <class '__main__.Car'>, <class 'object'>)

# the super().__init__() calls the __init__ of the FlyingCar class. Therefore, you need to pass the wing argument to the __init__ method.

# Because the FlyingCar class cannot access the __init__ method of the Car class, you need to initialize the doorand wheel attributes individually.