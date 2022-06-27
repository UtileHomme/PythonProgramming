class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0


counter = Counter()


counter.increment()
counter.increment()
counter.increment()

print(counter.value())

# The problem with above is that one can use the variable current and change its value anytime
# in the code outside the class as shown below

counter = Counter()

counter.increment()
counter.increment()
counter.current = -999

print(counter.value())

# To not allow that to happen, we can use private attributes. Use _variableName. This will say that
# the variable should not be manipulated outside the class as it may lead to a breaking change

class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0

counter = Counter()

counter.increment()
counter.increment()
counter.current = -999

print(counter.value())

# Double underscore (As below) ensures that the variables cannot be accessed outside the class

class Counter:
    def __init__(self):
        self.__current = 0

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current

    def reset(self):
        self.__current = 0


counter = Counter()

counter.increment()
counter.increment()
counter.increment()
counter.increment()

# This will give an error
# print(counter.__current)

# This is the resolution
print(counter._Counter__current)