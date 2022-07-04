guests = ['Jaimes', 'Mary', 'John', 'Patricia']

guests.sort()

print(guests)

# For sorting in reverse alphabetical order
guests.sort(reverse=True)

print(guests)

scores = [3, 1, 6, 3, 98, 5]

scores.sort()

print(scores)

# For sorting a list of tuples

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2020, 70.7)]


# We wish to sort the above by the third element in each tuples (revenue)

def sort_key(company):
    # Here we are saying that we wish to sort by the third index of the company element
    return company[2]


companies.sort(key=sort_key)

print(companies)

# Sorting a list with lambda

companies.sort(key=lambda company: company[2], reverse=True)

print(companies)
