

import re

text = 'Be careful and thoughtful, not forgetful'

pattern = r'\b\w+ful\b'

matches = re.findall(pattern, text)

print(matches)
