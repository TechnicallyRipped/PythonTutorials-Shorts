

# pip install pyshorteners
from pyshorteners import Shortener

x = Shortener()

url = "https://www.youtube.com/@TechnicallyRipped"

short_url = x.tinyurl.short(url)
print(short_url)