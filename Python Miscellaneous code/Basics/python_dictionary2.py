person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 25,
    'favourite_colors' : ['blue', 'green'],
    'active' : True
}

# 1. Looping all key values in a dictionary

print(person.items())

# 2. Iterate through all elements using for loop

for key , value in person.items():
    (f"{key} : {value}")
    
# 3. Looping through all keys


for key in person.keys():
    print(key)

# OR

for key in person:
    print(key)

# 4. Looping through all values

for values in person.values():
    print(values)
