# my_student = {
#     'name': 'Jatin',
#     'grades': [70, 88, 90, 99],
#     'average': None
# }
#
#
# def average_grade(student):
#     return sum(student['grades']) / len(student['grades'])


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def average(self):
        return sum(self.grade) / len(self.grade)


student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [91,22,44,55])

print(student_one.name)
print(student_two.name)
