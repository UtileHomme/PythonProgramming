friends = [
    {
        'name': 'Rolf',
        'location': 'Washington, D. C'
    },
    {
        'name': 'Anna',
        'location': 'Washington, D. C'
    },
    {
        'name': 'Charlie',
        'location': 'Washington, D. C'
    },
    {
        'name': 'Rolf',
        'location': 'San Francisco'
    }
]

your_location = input("Where are you right now? ")
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

# if len(friends_nearby) > 0:
#     print("You are not alone")

# Above if code is simulated version of below code:

# This will give a truthy or a True value if any friend is there in the same location as you
if any(friends_nearby):  # True if there is at least one friend and False if list is empty
    print("You are not alone")

"""
Values that evaluate to False    

0, 0.0
None
[], (), {}
False
"""

print(all([1, 2, 3, 4, 5]))

# 0 is false hence false
print(all([1, 2, 3, 4, 5, 0]))
