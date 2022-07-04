import re

s = "2021"
pattern = '\d{4}'

result = re.fullmatch(pattern, s)

print(result)

# However if the digits are in a long string it will return None

s = "released in 2021"

pattern = '\d{4}'

result = re.fullmatch(pattern, s)

print(result)

