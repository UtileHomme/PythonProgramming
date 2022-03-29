class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<Fixed Float {self.amount:.2f}>'

    # Calling the class magic methods and then
    def from_sum(self, value1, value2):
        return FixedFloat(value1 + value2)


number = FixedFloat(18.5764)
new_number = number.from_sum(19.574, 0.789)

# Output - <Fixed Float 18.58> <Fixed Float 20.36>
print(number, new_number)
