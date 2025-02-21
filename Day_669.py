

# pip install nltk
# import nltk
# nltk.download('words')

from nltk.corpus import words

l_words = set(word.lower() for word in words.words())

my_word = 'technicallyripped'

if my_word in l_words:
    print('Yes')
else:
    print('No') 

