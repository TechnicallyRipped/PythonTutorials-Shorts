

# pip install fuzzywuzzy

from fuzzywuzzy import process

choices = ['red','green','blue']

x = 'gran'

best_match = process.extractOne(x,choices)

print(best_match)







