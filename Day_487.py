

import re

text = "Hello, World! More text!"

pattern = r'[^\s]'

match = re.findall(pattern,text)

if match:
    print(match)
    print(len(match))
else:
    print('No matches found')