import csv

with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

# How to segregate the header of the csv and the data
with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):

        # If line no is 1, it is header
        if line_no == 1:
            print('Header')
            print(line)
            print('Data:')
        else:
            print(line)

# How to segregate the header of the csv and the data - USING NEXT() FUNCTION
with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.reader(f)

    # Skip the header line
    next(csv_reader)

    for line in csv_reader:
        print(line)
