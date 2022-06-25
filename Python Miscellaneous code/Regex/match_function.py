import re

l = [
    'Python',
    'CPython is an implementation',
    'Jython is an implementation'
]

# \w matches a single character
pattern = '\wython'

for s in l:
    result = re.match(pattern,s)
    print(result)