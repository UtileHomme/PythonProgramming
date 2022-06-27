class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('__del__ was called')


if __name__ == '__main__':
    person = Person('John Doe', 23)
    # since after below statement, person doesn't have a reference, del is called
    person = None

person = Person('John Doe', 23)
del person
