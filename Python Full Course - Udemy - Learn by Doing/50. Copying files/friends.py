# Ask the user for a list of 3 friends
# For each friend, we will tell the user whether they are nearby
# For each nearby friend, we will save their name to 'nearby_friends.txt'

# Split will give us ['Rolf', 'Jose', 'Charlie']
friends = input('Enter three friends names').split(',')

people = open('people.txt', 'r')

# Going to reach file but will give a list of each line one by one [line1, line2 etc.]
# .strip() is used to remove any empty line from the end of each name
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

# This gives us the people that match in both sets
friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()






