import re

price = 'Price: $189.50'

expression = 'Price: \$([0-9]*\.[0-9]*)'

matches = re.search(expression, price)

print(matches.group(0))  # entire match
print(matches.group(1))  # first thing in brackets

price_number = float(matches.group(1))
print(price_number)


