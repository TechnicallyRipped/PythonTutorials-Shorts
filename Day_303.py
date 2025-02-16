

# pip install nltk

from nltk import FreqDist
from nltk.tokenize import word_tokenize

text = '''Python is a great programming language.
        I really like Python because it makes 
        programming easy!'''
words = word_tokenize(text)

freq_dist = FreqDist(words)
print(freq_dist)

most_common = freq_dist.most_common()
print(most_common)

