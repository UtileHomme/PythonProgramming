accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


# default value of name is checking
def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance"""

    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.67, 'checking'),
    (-220.67, 'checking'),
    (-220.67, 'savings'),
]

for t in transactions:
    # add_balance(t[0], t[1])
    # named arguments
    add_balance(amount=t[0], name=t[1])

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Dictionary
users = [
    {
        'username': 'rolf', "password": '123'
    },
    {
        'username': 'teclado', "password": 'youaretoo'
    }
]

user_objects = [User(username=data['username'], password=data['password']) for data in users]

# Dictionary unpacking
user_objects = [User(**data) for data in users]


# List of Tuples
users = [
    (
        'rolf', '123'
    ),
    (
        'teclado','youaretoo'
    )
]

# Tuple unpacking
user_objects = [User(*data) for data in users]
