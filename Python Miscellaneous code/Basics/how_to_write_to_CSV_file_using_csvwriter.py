# How to write a data with headers and data into a csv file

import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', '652090', 'AF', 'AG']

# This injects a blank line
with open('countries1.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(data)

# To remove the blank line write below code
with open('countries2.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerow(data)

# Writing multiple rows to a CSV file

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries3.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)


