

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("The cat ran away.")

for t in doc:
    print(t.text, t.tag_)
    print(spacy.explain(t.tag_))

