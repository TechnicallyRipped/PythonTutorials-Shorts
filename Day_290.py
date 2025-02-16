


# pip install requests

import requests

url = "https://www.technicallyripped.com/test"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")


















