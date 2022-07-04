class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive

# Here the instance attributes in both classes have same definition

# The __init__() method of the SalesEmployee class has some parts that are the same as the ones in the __init__() method of the Employee class.
#
# To avoid duplication, you can call the __init__() method of Employee class from the __init__() method of the SalesEmployee class.
#
# To reference the Employee class in the SalesEmployee class, you use the super(). The super() returns a reference of the parent class from a child class.
#
# The following redefines the SalesEmployee class that uses the super() to call the __init__() method of the Employee class:

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.bonus + self.sales_incentive

# How to reuse methods using super

# The get_pay() method of the SalesEmployee class has some logic that is already defined in the get_pay() method of the Employee class. Therefore, you can reuse this logic in the get_pay() method of the SalesEmployee class.
#
# To do that, you can call the get_pay() method of the Employee class in the get_pay() method of SalesEmployee class as follows:

class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive

# Putting it all together

class Employee:
    def __init__(self, name, base_pay, bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus

    def get_pay(self):
        return self.base_pay + self.bonus


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, bonus, sales_incentive):
        super().__init__(name, base_pay, bonus)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return super().get_pay() + self.sales_incentive


if __name__ == '__main__':
    sales_employee = SalesEmployee('John', 5000, 1000, 2000)
    print(sales_employee.get_pay())  # 8000