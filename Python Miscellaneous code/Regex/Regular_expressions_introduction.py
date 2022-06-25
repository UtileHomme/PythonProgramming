import re

# How to find all digits in a string
p = re.compile('\d')

s = "Python 3.10 was released on October 04, 2011"

result = p.findall(s)

print(result)