

# pip install ddgs
from ddgs import DDGS

search = 'TechnicallyRipped'

with DDGS() as browser:
    results = browser.text(search, max_results=5)

# print(results)
for r in results:
    print(r['href'])

