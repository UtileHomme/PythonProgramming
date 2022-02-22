friends = ["Rolf", "ruth", "charlie", "Jen"]

time_since_seen = [3,7,15,11]

# Dictionary of elements
long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

# Output - {'ruth': 7, 'charlie': 15, 'Jen': 11}
print(long_timers)