# https://www.youtube.com/watch?v=W7QByFjVom8


# OLD method of reading files
movies = [
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Green Book", "director": "abc"},
    {"name": "Amadeus", "director": "Forman"},
]


def write_to_file(output):
    with open("file.csv", "w") as f:
        f.write("name,director \n")
        for line in output:
            f.write(f"{line['name']}, {line['director']}\n")


def read_from_file():
    with open("file.csv", "r") as f:
        content = f.readlines()

        # Omit the header
        for line in content[1:]:
            # Split the line into arrays using delimiter ,
            columns = line.strip().split(",")
            print(f"Name: {columns[0]} \tDirector: {columns[1]}")
