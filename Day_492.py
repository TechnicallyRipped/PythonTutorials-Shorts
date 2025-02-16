

import re

text = "abcABC123!@#$%^&*()_+=-"

pattern = r'[^a-zA-Z0-9]'

matches = re.findall(pattern, text)

print(matches)
