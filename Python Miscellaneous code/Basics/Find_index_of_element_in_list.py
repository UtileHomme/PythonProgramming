cities = ['a', 'b', 'c', 'd']

city = 'e'

if city in cities:
    result = cities.index(city)
    print(f'The {city} has index {result}')
else:
    print(f'The city {city} doesnot exist in the list')
