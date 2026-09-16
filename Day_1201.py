


import spacy

nlp = spacy.load("en_core_web_md")

s1 = nlp('Dogs are cool!')
s2 = nlp('Dogs have ears.')

print(s1.similarity(s2))
