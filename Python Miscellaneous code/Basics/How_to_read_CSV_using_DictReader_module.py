import csv

with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    next(csv_reader)

    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")

# How to specify customized Headers

print("gap")

fieldnames = ['country_name', 'area', 'code2', 'code3']

with open('country.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)

    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")