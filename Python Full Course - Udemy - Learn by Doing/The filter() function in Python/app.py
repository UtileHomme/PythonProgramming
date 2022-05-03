friends = ["Rolf", "jose", "Randy", "Anna", "mary"]


# Get friends which start only with r
def starts_with_r(friend):
    # https: // www.w3schools.com / python / ref_string_startswith.asp
    return friend.startswith("R")


# arg 1 : function that returns True or False
# https://www.geeksforgeeks.org/filter-in-python/

# arg 2:  Argument for the function
start_with_r = filter(starts_with_r, friends)

# Output
# Rolf
# Randy
# Traceback (most recent call last):
#   File "C:/Users/jsharma029/OneDrive/Study Related/Python/Python Full Course - Udemy - Learn by Doing/The filter() function in Python/app.py", line 18, in <module>
#     print(next(start_with_r))
# StopIteration
# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

print(list(start_with_r))
