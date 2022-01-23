students = [
    {"name" : "Rolf" , "grade" : 90},
    {"name" : "Bob" , "grade" : 90},
    {"name" : "Anne" , "grade" : 90},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")
