class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)

print(john is jane)  # False

print(john == jane) # False

# We want to compare the value of age and if they are equal, the above print statements should return false

# To resolve this, we can implement the _eq_ dunder method

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # we are comparing the ages of the two objects and if they are equal, we return false
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.age == other.age

        return False


john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
mary = Person('Mary', 'Doe', 27)

print(john == jane)  # True
print(john == mary)  # False


john = Person('John', 'Doe', 25)
print(john == 20)  # False