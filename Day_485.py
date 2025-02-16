


import re

text = "Hello World! This is text."

pattern = r"world"

match = re.search(pattern, text)

if match:
    print("Pattern found")
    print(f"Start: {match.start()}")
    print(f"End: {match.end()}")
else:
    print("Pattern not found")
