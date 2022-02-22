friends = ["Rolf", "ruth", "charlie", "Jen"]

guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# This converts all values to lower case
friends_lower = [f.lower() for f in friends]

# finding common people using list comprehension
present_friends = [name.title() for name in guests if name.lower() in friends_lower]

print(present_friends)