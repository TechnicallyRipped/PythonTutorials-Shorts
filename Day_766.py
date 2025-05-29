

# pip install fuzzywuzzy

from fuzzywuzzy import fuzz

word = 'apple'

x1 = 'appel'
x2 = 'banana'
x3 = 'apple'

print(fuzz.ratio(x1,word))
print(fuzz.ratio(x2,word))
print(fuzz.ratio(x3,word))




