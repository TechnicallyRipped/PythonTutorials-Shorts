

import re

text = "Maria went to the opera."

pattern = r'\b\w*a\b'

matches = re.findall(pattern, text)

print(matches)
