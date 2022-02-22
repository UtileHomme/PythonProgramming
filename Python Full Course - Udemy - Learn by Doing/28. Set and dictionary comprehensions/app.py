friends = ["Rolf", "ruth", "charlie", "Jen"]

guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# This converts all values to lower case converted to sets
friends_lower = {f.lower() for f in friends}

guests_lower = {g.lower() for g in guests}

# this prints the people common to both lists
present_friends = friends_lower.intersection(guests_lower)

present_friends = {name.title() for name in present_friends}

# Output - {'Charlie', 'Rolf'}
print(present_friends)