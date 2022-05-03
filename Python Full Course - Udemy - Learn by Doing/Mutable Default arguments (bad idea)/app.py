def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


a1 = create_account('checking', 'Rolf')

# Output - {'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen']}
# Problem - Rolf is also appended to the list even though it is a new account
a2 = create_account('savings', 'Jen')

print(a2)
