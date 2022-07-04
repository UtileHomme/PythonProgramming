class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


john = Person('John', 18)

john.age = -1

# age = -1
# if age <= 0:
#     raise ValueError('The age must be positive')
# else:
#     john.age = age

# We have to do the above everytime for each parameter. Solution is to define getters
# and setters

class Person:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)

    def set_age(self,age):
        if age<=0:
            raise ValueError('The age must be positive')
        self.age = age

    def get_age(self):
        # _age is a private attribute
        return self._age

# How to use Property function to define a property for the class

from pprint import pprint


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age <= 0:
            raise ValueError('The age must be positive')
        # _age is a private attribute
        self._age = age

    def get_age(self):
        # _age is a private attribute
        return self._age

    age = property(fget=get_age, fset=set_age)


print(Person.age)

john = Person('John', 18)
pprint(john.__dict__)
pprint(john._age)

john.age = 19
pprint(Person.__dict__)
pprint(Person.age)


