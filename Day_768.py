

# pip install fuzzywuzzy

from fuzzywuzzy import fuzz

long = 'Hello World, how are you'

short = 'Hello World'

score = fuzz.partial_ratio(long,short)
print(score)







