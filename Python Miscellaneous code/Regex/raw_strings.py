# When we want to inject a backlash (literally) in a pattern, we use raw strings

import re

s = '\section'

pattern = r'\\section'

result = re.findall(pattern, s)

print(result)