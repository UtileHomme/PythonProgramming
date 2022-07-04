import csv

outfile = open('student_names.csv', 'w')
outfile_header = "Student First Name, Student Last Name\n"
outfile.write(outfile_header)

with open("student_grades.csv", 'r') as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    print(header)

    for row in reader:
        student_first_name = row[0]
        student_last_name = row[1]
        student_year = row[2]
        student_grade = row[3]
        print(student_first_name, student_last_name, student_year, student_grade)
        line = "{}, {} \n".format(student_first_name, student_last_name)
        outfile.write(line)

    outfile.close

