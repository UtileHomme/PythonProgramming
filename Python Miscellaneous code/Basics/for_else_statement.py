# If a break is encountered in for loop, else will not run

# Scenario

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Jatin', 'age': 25},
    {'name': 'Sharma', 'age': 25},
]

name = input('Enter your name: ')

found = False
for person in people:
    if person['name'] == name:
        found = True
        print(person)
        break

if not found:
    print(f'{name} not found!')

# Better way of doing this with for else and without the flag found

name = input('Enter your name: ')

for person in people:
    if person['name'] == name:
        print(person)
        break

else:
    print(f'{name} not found!')