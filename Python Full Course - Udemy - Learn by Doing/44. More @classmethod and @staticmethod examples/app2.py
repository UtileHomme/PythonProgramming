class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<Fixed Float {self.amount:.2f}>'

    # Calling the class magic methods using recursion
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


# We no longer need to defined an object first
new_number = FixedFloat.from_sum(19.574, 0.789)

# Output - <Fixed Float 18.58> <Fixed Float 20.36>
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '$'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro(18.786)
# Output - <Euro $18.79>
print(money)

# Output -  <Euro $58.40>
money1 = Euro.from_sum(13.1, 45.3)
print(money1)
