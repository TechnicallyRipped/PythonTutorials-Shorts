

import re

text = 'Hello world! How are you? I am fine! How about you?'

pattern = r'[^.?!]*[?]'

matches = re.findall(pattern, text)

print(matches)
