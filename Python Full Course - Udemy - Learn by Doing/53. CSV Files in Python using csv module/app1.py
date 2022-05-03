# https://www.youtube.com/watch?v=W7QByFjVom8

import csv

# Using CSV modules for reading and writing files
movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "abc"},
    {"name": "Amadeus", "director": "Forman"},
]


def write_to_file(output):
    with open("file.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'director'])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open("file.csv", "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            print(f"Name: {line['name']} \tDirector: {line['director']}")


write_to_file(movies)
read_from_file()
