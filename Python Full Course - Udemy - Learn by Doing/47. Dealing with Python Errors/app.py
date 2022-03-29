class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        # Is instance tells if car is an instance of Car or not
        if not isinstance(car, Car):
            raise TypeError(
                f'Tried to add a `{car.__class__.__name__}` to the garage, but you can add only `Car` objects.')
        self.cars.append(car)

        # raise NotImplementedError('We cant add cars to the garage yet')


ford = Garage()
carss = Car('Ford', 'Fiesta')

try:
    ford.add_car('carss')
except TypeError:
    print('Your car was not an Car!')
