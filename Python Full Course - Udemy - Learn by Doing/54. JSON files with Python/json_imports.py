import json

file = open('friends.txt', 'r')

# json.load takes a file pointer and converts file_contents into dictionary
file_contents = json.load(file)

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars.txt', 'w')
json.dump(cars, file)
file.close()

# List of Strings
my_json_string = '[{"name" : "Alfa Romeo", "released" : 1950}]'

# Converts Json into dictionary
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])