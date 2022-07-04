# The following example uses the \d\d to match two digits in a time string:

import re

time = '12:20'
matches = re.finditer('\d\d', time)
for match in matches:
    print(match.group())

# If you use the caret anchor (^), you’ll get one group which is the two digits at the beginning of the string. For example:

import re

time = '12:20'

# This will match the first two digits in a string
matches = re.finditer('^\d\d', time)
for match in matches:
    print(match.group())

# Similarly, if you use the $ anchor, you’ll get the last two digits because the $ matches \d\d at the end of the time string:

import re

time = '12:20'
matches = re.finditer('\d\d$', time)
for match in matches:
    print(match.group())

# To match for a particular format
import re

# String should start with two digits and end with two digits and should only have column in between
time = '12:20'
matches = re.finditer('^\d\d:\d\d$', time)
for match in matches:
    print(match.group())

    


