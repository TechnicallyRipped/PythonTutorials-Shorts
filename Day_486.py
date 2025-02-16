

import re

text = "Hello World! Hello all!"

pattern = r"Hello"

match = re.findall(pattern, text)

if match:
    print("Pattern found")
    print(match)
    print(f"Matches {len(match)}")
else:
    print("Pattern not found")
