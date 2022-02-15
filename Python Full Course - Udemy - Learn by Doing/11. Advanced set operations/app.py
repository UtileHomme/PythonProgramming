# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412522#overview

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print(art_but_not_science)
print(science_but_not_art)

# What members are not in boh sets

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# What members are in both sets
art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# Combine both sets
all_friends = art_friends.union(science_friends)
print(all_friends)