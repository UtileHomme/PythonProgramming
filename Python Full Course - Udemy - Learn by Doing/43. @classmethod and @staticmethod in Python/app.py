class Student:
    # This is an instance method.. this takes the object as the first argument
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

print(rolf.average())


class Foo:
    # class method..this takes class as an argument
    @classmethod
    def hi(cls):
        # Printing the classes name
        # Output - Foo
        print(cls.__name__)


my_object = Foo()
my_object.hi()


class Bar:
    # Doesn't use the current object but is related to the class
    @staticmethod
    def hi():
        print('Hello, I don\'t take any parameters')


another_object = Bar()
another_object.hi()
