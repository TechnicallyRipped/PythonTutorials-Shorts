



import re

text = 'Call 123-456-7890, not 098-765-4321'

pattern = r'\b\d{3}-\d{3}-\d{4}\b'

matches = re.findall(pattern, text)

print(matches)
