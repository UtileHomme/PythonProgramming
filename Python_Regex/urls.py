import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# ? mark makes the s optional
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Groups are indexed with the number of parentheses
# Group 0 is the entire match
# Group 1 is (www\.)
# Group 2 is (\w+)
# Group 3 is (\.\w+)

matches = pattern.finditer(urls)

# Output
#
# https://www.google.com
# http://coreyms.com
# https://youtube.com
# https://www.nasa.gov

# for match in matches:
#     print(match.group(0))

# Output

# www.
# None
# None
# www.

# for match in matches:
#     print(match.group(1))

# google
# coreyms
# youtube
# nasa
# for match in matches:
#     print(match.group(2))

# .com
# .com
# .com
# .gov
for match in matches:
    print(match.group(3))

#we want to use this method to get the substring in the URL depending on group
subbed_urls = pattern.sub(r'\2\3', urls)

# google.com
# coreyms.com
# youtube.com
# nasa.gov
print(subbed_urls)
