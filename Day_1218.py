

# pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("name")
password = os.getenv("password")

print(username)
print(password)