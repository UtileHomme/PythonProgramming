# Define a class

class Person:
    pass


# define object

person = Person()


# defining instance attributes and functions

class Person1:

    # below are instance attribules - name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, it's {self.name}"


personObject = Person1('John', 25)

print(personObject.name, personObject.greet())


# defining class attributes and functions

class Person1:
    # counter is a class attribute which is shared by all objects
    counter = 0

    # below are instance attribules - name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person1.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}"


personObject = Person1('John', 25)
personObject1 = Person1('John1', 25)

print(personObject.name, personObject.greet(), Person1.counter)


# Defining a class Method

# A class method is shared by all instances of a class

class Person1:
    # counter is a class attribute which is shared by all objects
    counter = 0

    # below are instance attribules - name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person1.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}"

    @classmethod
    def create_anonymous(cls):
        return Person1('Anonymous', 22)


anonymous = Person1.create_anonymous()
print(anonymous.name)


# Definining a static method

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9 * c / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5 * (f - 32) / 9


f = TemperatureConverter.celsius_to_fahrenheit(30)
print(f)


# Inheritance

class Employee(Person1):
    def __init__(self, name, age, job_title):
        # this is important
        super().__init__(name, age)
        self.job_title = job_title

    # Overriding the parent classes greet method
    def greet(self):
        return super().greet() + f" I am a {self.job_title}"


employee = Employee('John', 25, 'Python Developer')
print(employee.greet())
