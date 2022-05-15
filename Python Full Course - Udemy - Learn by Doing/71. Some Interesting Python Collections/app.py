# A queue where you can add or remove things from either side is called deque or double ended queue
# Else it is called queue

# In a stack you add or remove from the same end

# Counter Usage

from collections import Counter

device_temperatures = [13.5, 14.0, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)

# 1
print(temperature_counter[14.0])

print(Counter({'hello': 5, 'hi': 3})['hi'])


