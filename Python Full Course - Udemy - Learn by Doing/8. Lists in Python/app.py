# https://www.udemy.com/course/the-complete-python-course/learn/lecture/9412520#overview

friends = ["Rolf", "Bob", "Anne"] #Lists

# add new elements to the list
friends.append("Jen")

friends.remove("Bob")
# friends.remove(["Bob", "Rolf"])

# For accessing lists
print(friends[0])
print(friends)

# Length of the list
print(len(friends))

# List of lists
friends1 = [
    ["Rolf", 24],
    ["Bob", 30],
    ["Anne", 27]
]

friends1.remove(["Bob", 30])

print(friends1[0][1])
print(friends1)


