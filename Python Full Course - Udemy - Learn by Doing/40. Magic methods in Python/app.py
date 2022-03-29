class Student:
    def __init__(self, name):
        self.name = name

movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)
print("hi".__class__)

print(len(movies))

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford.cars)

# Garage.__len__(ford)
print(len(ford))

# Garage.__getitem__(ford,0)
print(ford[0])

for car in ford:
    print(car)

# __str__ function is called
print(ford)