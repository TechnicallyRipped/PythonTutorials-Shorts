


import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp('I uploaded a video about Spacy.')

filtered = [
    token.text for token in doc if not token.is_stop
    ]

clean_text = " ".join(filtered)

print(clean_text)