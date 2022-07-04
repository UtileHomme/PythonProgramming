class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    age = property(fget=get_age)

john = Person('John', 25)
print(john.age)

print(john.get_age())

# We are able to get the value of age using the variable and the function. This is redundant

# We can rename the get_age function as age() as below using property decorator

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

# A similar thing can be done for setters also

# Old Way
class Person:
    def __init__(self, name, age):
        self.name = name
        # _age is a private attribute
        self._age = age

    @property
    def age(self):
        return self._age

    def set_age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')

        # _age is a private attribute
        self._age = value

# New Way

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        # _age is a private attribute
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        # _age is a private attribute
        self._age = value

# Summary of how to use property decorator

class MyClass:
    def __init__(self, attr):
        self.prop = attr

    @property
    def prop(self):
        return self.__attr

    @prop.setter
    def prop(self, value):
        self.__attr = value

# Another example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('The age must be positive')
        self._age = value

    @property
    def name(self):
        return self._age

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('The name cannot be empty')
        self._age = value

p = Person('Jatin', 43)
print(Person.age)

