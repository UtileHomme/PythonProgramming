class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, it's {self.name}"

class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

employee = Employee('John', 'Python Developer')
print(employee.greet())

# type vs isinstance

person = Person('Jane')
print(type(person))

employee = Employee('John', 'Python Developer')
print(type(employee))

# To check if an object is an instance of a class, you use the isinstance() method. For example:

person = Person('Jane')
print(isinstance(person, Person))  # True

employee = Employee('John', 'Python Developer')
print(isinstance(employee, Person))  # True
print(isinstance(employee, Employee))  # True
print(isinstance(person, Employee))  # False

# issubclass function

class SalesEmployee(Employee):
    pass

print(issubclass(SalesEmployee, Employee)) # True
print(issubclass(SalesEmployee, Person)) # True

# Note that when you define a class that doesn’t inherit from any class, it’ll implicitly inherit from the built-in object class.

print(issubclass(Person, object)) # True

