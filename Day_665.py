

# pip install nltk
# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from nltk.corpus import wordnet

word = "increase"
synonyms = set()

for syn in wordnet.synsets(word):
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

print(synonyms)



