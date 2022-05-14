# Named tuple usage
# The Keys and the values will each have a name as well

from collections import namedtuple

# account = ('checking', 1860.99)
#
# print(account[0])  # name
# print(account[1])  # balance

Account = namedtuple('Account', ['name', 'balance'])

# named arguments
account = Account('checking', balance = 1867)

print(account.name)
print(account.balance)
print(account)

accountNamedTuple = Account._make(account)

# Other way of doing above
# accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict()['balance'])








