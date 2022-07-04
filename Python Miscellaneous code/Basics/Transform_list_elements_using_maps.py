# Conventional way of doubling the elements of a list

bonuses = [100, 200, 300]

new_bonuses = []

for bonus in bonuses:
    new_bonuses.append(bonus + 2)

print(new_bonuses)

# Using map as iterator

iterator = map(lambda bonus: bonus * 2, bonuses)

print(list(iterator))

# map as iterator example 2

names = ['david', 'peter', 'jenneifer']

new_names = map(lambda name: name.capitalize(), names)

print(list(new_names))

