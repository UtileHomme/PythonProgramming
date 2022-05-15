friends = ["Rolf", "jose", "Randy", "Anna", "mary"]


# Get friends which start only with r
def starts_with_r(friend):
    # https: // www.w3schools.com / python / ref_string_startswith.asp
    return friend.startswith("R")


# arg 1 : function that returns True or False
# https://www.geeksforgeeks.org/filter-in-python/

# arg 2:  Argument for the function
start_with_r = filter(lambda friend: friend.startswith("R"), friends)

# Above code is simulated version of the below cose
another_starts_with_r = (f for f in friends if f.startswith("R"))


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


print(list(start_with_r))
