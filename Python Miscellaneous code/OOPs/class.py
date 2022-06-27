class Person:
    pass

person = Person()

# True
# checks if the object person is an instance of Class Person
print(isinstance(person, Person))

# How to find the name of the class
# Person
print(Person.__name__)