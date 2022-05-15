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
    # Each element of T will be passed a separate argument
    add_balance(*t)

