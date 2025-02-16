

import re

text = "apples are a tasty fruit"

pattern = r'\ba\w*'

matches = re.findall(pattern, text)

print(matches)
