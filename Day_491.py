

import re

text = "0123456789abc"

pattern = r'[^4-7]'

matches = re.findall(pattern, text)

print(matches)
