



import spacy

nlp = spacy.load("en_core_web_sm")


with open('example_text.txt') as f:
    text = f.read()

doc = nlp(text)

for sentence in doc.sents:
    print(sentence.text)