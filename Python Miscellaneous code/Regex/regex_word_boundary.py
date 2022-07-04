import re

s = 'CPython is the implementation of Python in C'

# This looks for word Python, even if it occurs as substring of another word
matches = re.finditer('Python', s)
for match in matches:
    print(match.group())

# This searches for Python word as a whole
s = 'CPython is the implementation of Python in C'
matches = re.finditer(r'\bPython\b', s)
for match in matches:
    print(match.group())
