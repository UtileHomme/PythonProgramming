# 1. Digit character set

# How to match all single digits in a string

import re

s = 'Python 3.0 was released in 2008'
matches = re.finditer('\d', s)
for match in matches:
    print(match.group())

# Output of above

# 3
# 0
# 2
# 0
# 0
# 8

# To match a group of two digits, use below

import re

s = 'Python 3.0 was released in 2008'
matches = re.finditer('\d\d', s)

# 20
# 08
for match in matches:
    print(match.group())

# 2. Word Character set

# Regular expressions use \w to represent the word character set. The \w matches a single ASCII character including Latin alphabet, digit, and underscore (_)

import re

s = 'Python 3.0'
matches = re.finditer('\w', s)
for match in matches:
    print(match.group())

# *** Notice that the whitespace and . are not included in the matches.

# P
# y
# t
# h
# o
# n
# 3
# 0

# 3. Whitespace character set

# The \s matches whitespace including a space, a tab, a newline, a carriage return, and a vertical tab.

import re

s = ' Python 3.0'
matches = re.finditer('\s', s)
for match in matches:
    print(match)

# <re.Match object; span=(0, 1), match=' '>
# <re.Match object; span=(7, 8), match=' '>

# 4. Inverse Character Set

# \D	Match a single character except for a digit
# \W	Match a single character that is not a word character
# \S	Match a single character except for whitespace

import re

phone_no = '+1-(650)-513-0514'
matches = re.finditer('\D', phone_no)
for match in matches:
    print(match.group())

# +
# -
# (
# )
# -
# -

import re

# To turn the phone number +1-(650)-513-0514 into the 16505130514, you can use the sub() function:
phone_no = re.sub('\D', '', '+1-(650)-513-0514')
print(phone_no)

# The .(dot) character set

# The dot (.) character set matches any single character except the new line (\n)

import re

version = "Python\n4"
matches = re.finditer('.', version)
for match in matches:
    print(match.group())

# P
# y
# t
# h
# o
# n
# 4





