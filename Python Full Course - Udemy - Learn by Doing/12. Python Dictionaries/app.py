# Dictionaries keep the order in which they are added

friend_ages = {"Rolf": 24, "Adam": 30, "Anne" : 27}

friend_ages["Bob"] = 20

print(friend_ages["Bob"])
print(friend_ages)

# tuple with multiple elements
friends = (
    {"name": "Rolf Smith", "age" : 24},
    {"name": "Adam Wolf", "age" : 30},
    {"name": "Anne Pun", "age" : 27}
)

print(friends[0]["name"])

# OR

friend = friends[0]

print(friend["name"])

# How to get a dictionary out of a List

friends1 = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages1 = dict(friends1)
print(friend_ages1)