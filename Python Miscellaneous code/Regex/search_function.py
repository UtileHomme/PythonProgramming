import re

s = "Python 3.10 was released on October 04, 2011"

# Finds the first two matching digits
pattern = '\d{2}'

match = re.search(pattern, s)

print('Matched string: ', match.group())
print('Starting Position: ', match.start())
print('Ending Position: ', match.end())
print('Positions: ', match.span())
