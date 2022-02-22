friends = ["Rolf", "ruth", "charlie", "Jen"]

guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# This converts all values to lower case
friends_lower = set([f.lower() for f in friends])

guests_lower = set([g.lower() for g in guests])

# this prints the people common to both lists
print(friends_lower.intersection(guests_lower))