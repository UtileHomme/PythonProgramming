movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "A beatiful day in the neighbourhood", "director": "Heller"},
    {"name": "The Irishman", "director": "Scorsese"}
]

def find_movie(finder):
    for movie in movies:
        print(finder(movie))
#

def find_movie1(expected, finder):
    for movie in movies:
        if finder(movie) == expected:
            return movie


find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for?")

find_movie(lambda movie: movie[find_by])

find_by = input("What property are we searching by? ")
looking_for = input("What are you looking for?")

movieName = find_movie1(looking_for, lambda movie: movie[find_by])
print(movieName)

