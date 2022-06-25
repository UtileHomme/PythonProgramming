import csv

fieldnames = ['name', 'area', 'country_code2', 'country_code3']

rows = [
    {
        'name': 'Albania',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALB'
    },
    {
        'name': 'Algeria',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALG'
    }, {
        'name': 'American Sam',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'AMS'
    }
]

with open('countries4.csv', 'w', encoding='UTF-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
