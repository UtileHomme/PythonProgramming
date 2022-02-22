def average(seq):
    return sum(seq) / len(seq)


avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average" : avg,
    "total" : total,
    "top" : top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Rolf1", "grades": (67, 90, 95, 200)}
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total' or 'top")

    if operation == "average":
        print(avg(grades))
    elif operation == "total":
        print(total(grades))
    elif operation == "top":
        print(top(grades))
