



import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Python is the best!")

for token in doc:
    print(token.text)