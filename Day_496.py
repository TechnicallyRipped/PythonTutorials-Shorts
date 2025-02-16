

import re

text = 'To prepare the meal, preheat the oven'

pattern = r'\bpre\w*\b'

matches = re.findall(pattern, text)

print(matches)
