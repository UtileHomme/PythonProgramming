# Conventional way
# def average(sequence):
#     return sum(sequence) / len(sequence)

average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Rolf1", "grades": (67, 90, 95, 200)}
]

for student in students:
    print(average(student["grades"]))
