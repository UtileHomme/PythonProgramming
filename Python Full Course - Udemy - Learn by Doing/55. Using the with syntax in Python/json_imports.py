import json

with open('friends.txt', 'r') as file:
    # json.load takes a file pointer and converts file_contents into dictionary
    file_contents = json.load(file)

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars.txt', 'w') as file:
    json.dump(cars, file)


# List of Strings
my_json_string = '[{"name" : "Alfa Romeo", "released" : 1950}]'

# Converts Json into dictionary
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])
