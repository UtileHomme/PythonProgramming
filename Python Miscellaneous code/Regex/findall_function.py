import re

s = "Python 3.10 was released on October 04, 2011"

result = re.findall('\d',s)

print(result)