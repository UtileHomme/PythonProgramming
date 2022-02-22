friends = ["Rolf", "ruth", "charlie", "Jen"]

time_since_seen = [3,7,15,11]

# zip combines one or more lists into a combined list
long_timers = list(zip(friends, time_since_seen))

long_timers1 = dict(zip(friends, time_since_seen))

# [('Rolf', 3), ('ruth', 7), ('charlie', 15), ('Jen', 11)]
print(long_timers)

# {'Rolf': 3, 'ruth': 7, 'charlie': 15, 'Jen': 11}
print(long_timers1)
