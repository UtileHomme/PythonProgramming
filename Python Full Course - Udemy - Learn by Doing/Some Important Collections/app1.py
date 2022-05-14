# Default Dict usage
# It never raises a index not found error. Instead it creates an empty value at that place

from collections import defaultdict

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge')]

# Let's say we want to create the below dictionary

{
    'Rolf': ['MIT', 'Cambridge'],
    'Jen': ['Oxford']
}

# Not the preferred ways

# alma_mater = {}

# for coworker in coworkers:
#
#     if coworker[0] not in alma_mater:
#         alma_mater[coworker[0]] = []
#
#     alma_mater[coworker[0]].append(coworker[1])

# Not the preferred ways
# for coworker, place in coworkers:
#
#     if coworker not in alma_mater:
#         alma_mater[coworker] = []
#
#     alma_mater[coworker].append(place)

# default dict gives us a new list
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    alma_maters[coworker].append(place)

# ['MIT', 'Cambridge']
print(alma_maters['Rolf'])

# []
print(alma_maters['Anne'])
