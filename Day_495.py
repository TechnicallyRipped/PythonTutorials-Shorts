

import re

text = 'Hello World!'

pattern = r'hello'

matches = re.findall(pattern, text,
                     re.IGNORECASE)

print(matches)
