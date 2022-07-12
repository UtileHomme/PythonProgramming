class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    # This is a getter
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

# Property decorator allows the methods to be accessed as an attribute
# We are trying to use the setter method to first and last attributes using the fullname function
emp_1.fullname = "Corey Schafer"

print(emp_1.first)

# Email method is being accessed as an attribute
print(emp_1.email)

# Full Name method is being accessed as an attribute
print(emp_1.fullname)

# Calling the deleter function with same name using del
del emp_1.fullname

print(emp_1.first)
