

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Joe works at Apple as a Data Scientist.")

for e in doc.ents:
    print(e.text, e.label_)