# sets do not hold sort order. They also do not have duplicates

art_friends = {"Rolf", "Anne"}
science_friends = ("Jen", "Charlie")

art_friends.add( "Jen")

print(art_friends)

# How to remove elements from a set
art_friends.remove("Jen")

print(art_friends)