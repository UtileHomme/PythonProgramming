class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person = Person('John', 25)
    print(bool(person))

# By default, the default bool value of the object will be True

# To customize the same, implement the __bool__ method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __bool__(self):
        if self.age < 18 or self.age > 65:
            return False
        return True


if __name__ == '__main__':
    person = Person('Jane', 16)
    print(bool(person))  #

# Implementing the len method

# If a custom class doesn’t have the __bool__ method, Python will look for the __len__() method. If the __len__ is zero, the object is False. Otherwise, it’s True.
#
# If a class doesn’t implement the __bool__ and __len__ methods, the objects of the class will evaluate to True.

class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print('len was called...')
        return self.length


if __name__ == '__main__':
    payroll = Payroll(0)
    print(bool(payroll))  # False

    payroll.length = 10
    print(bool(payroll))  # True

