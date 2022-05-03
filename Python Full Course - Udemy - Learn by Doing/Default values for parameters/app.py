accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}

# default value of name is checking
def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the new balance"""

    accounts[name] += amount
    return accounts[name]


add_balance(500.00, 'savings')
add_balance(500.00)

print(accounts['savings'])
print(accounts['checking'])
