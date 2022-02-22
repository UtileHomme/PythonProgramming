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


def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

'''
OUTPUT
Ford Fiesta does 50.0 miles per gallon.
Ford1 Fiesta1 does 50.0 miles per gallon.
'''
for car in cars:
    calculate_mpg(car)
