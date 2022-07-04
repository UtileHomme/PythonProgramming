class Item:

    # these are class attributes which have the same state for all objects
    pay_rate = 0.8  # The pay rate after 20% discount

    # Whatever values are added to the all list will have the latest / updated values for all objects
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        # Class attributes can be directly accessed by the class
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # This magic method helps represent the object in a human readable format
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)

# Gives all attributes for Class Level
print(Item.__dict__)

# Gives all attributes for object level
print(item1.__dict__)
