short_tuple = ("Rolf", "Bob")

a_bit_clearer = ("Rolf", "Bob")

tuple_inside_list = [("Rolf", "Bob")]

friends = ("Rolf", "Bob", "Anne")

# This won't work. You cannot append using a function
# friends.append("Jen")

# To do add a new element to a tuple

friends = friends + ("Jen",)

print(friends)
