cars = [
    {
        "make": "Ford",
        "model": "Fiesta",
        "mileage": 23000,
        "fuel_consumed": 460
    },
    {
        "make": "Ford1",
        "model": "Fiesta1",
        "mileage": 2300,
        "fuel_consumed": 46
    }
]


def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    print(f"{name} does {mpg} miles per gallon")


'''
OUTPUT
Ford Fiesta does 50.0 miles per gallon.
Ford1 Fiesta1 does 50.0 miles per gallon.
'''
for car in cars:
    mpg = print_car_info(car)
