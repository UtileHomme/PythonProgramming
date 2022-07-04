from abc import ABCMeta, abstractmethod


# Animal is now an abstract Class
class Animal(metaclass=ABCMeta):
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    # This method has to be implemented since it was an abstract method in Animal and Dog is inheriting from Animal
    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


d = Dog('scooby')
print(d.walk())

animals = [Dog('Rolf'), Monkey('Bob')]
for a in animals:
    print(isinstance(a, Animal))
    print(a.num_legs())
