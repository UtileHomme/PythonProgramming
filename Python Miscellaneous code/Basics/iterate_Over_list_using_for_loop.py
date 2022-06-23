cities = ['New York', 'beijing', 'Cairo']

for city in cities:
    print(city)
    
#  Using enumerate to get the index as well
for index, city in enumerate(cities):
    print(f"{index} and {city}")