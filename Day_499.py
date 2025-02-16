

import re

text = "hi, tech, rip, ball, code, super, python"

pattern = r'\b\w{4}\b'

matches = re.findall(pattern, text)

print(matches)








