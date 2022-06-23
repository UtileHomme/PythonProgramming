person = {
    'first_name' : 'John',
    'last_name' : 'Doe',
    'age' : 25,
    'favourite_colors' : ['blue', 'green'],
    'active' : True
}

# 1. Accessing values in a dictionary
print(person['first_name'])

# 2. Accessing values in a dictionary without throwing a key not found error
firstName = person.get('first_name')

print(firstName)

# The above returns NONE if the index doesn't exist

# 3. Accessing values in a dictionary without throwing a key not found error and setting a default value
firstName1 = person.get('f_name', 'Jatin Sharma')

print(firstName1)

# The above returns the default value is the key doesn't exist

# 4. Adding new values to a dictionary

person['gender'] = 'Female'

print(person)

# 5. Modifying existing values  to a dictionary

person['gender'] = 'Male'

print(person)

# 6. Removing key values pairs

del person['gender']

print(person)

