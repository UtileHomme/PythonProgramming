import re

email = 'jatins368@gmail.com'
expression = '[a-z]+'

# ['jatins', 'gmail', 'com']
matches = re.findall(expression, email)
print(matches)

name = matches[0]

domain = f'{matches[1],matches[2]}'

# jatins ('gmail', 'com')
print(name, domain)



