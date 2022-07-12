class Employee:
    # class variables can be accessed either using Class or the instance
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # OR
        # self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1.pay)
print(Employee.raise_amount)
emp_1.apply_raise()

print(emp_1.raise_amount)

emp_2.raise_amount = 1.05

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.raise_amount)

# The instance doesn't have raise amount since it is a class variable
print(emp_1.__dict__)

print(Employee.__dict__)

print(emp_2.__dict__)

print(Employee.__dict__)

# Because 2 instances were created, the value of num_of_emps is 2
print(Employee.num_of_emps)
