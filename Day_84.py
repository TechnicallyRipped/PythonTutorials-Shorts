

import requests
import json


response = requests.get('https://api.thecatapi.com/v1/images/search')


if response.status_code == 200:

    data = json.loads(response.text)

    image_url = data[0]['url']
    print(image_url)






























