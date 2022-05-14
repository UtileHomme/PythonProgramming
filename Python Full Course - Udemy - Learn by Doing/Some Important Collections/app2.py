# Default Dict usage
# It never raises a index not found error. Instead it creates an empty value at that place

from collections import defaultdict

my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']

other_coworkders = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

# Expectation
# coworker_companies = {'Jen': 'Teclado', 'Rolf' : 'Apple Inc'}

# Set's a default value for a person in case there name or company is not mentioned in the coworkers dictionary
coworker_companies = defaultdict(lambda: my_company)

for person, company in other_coworkders:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])

