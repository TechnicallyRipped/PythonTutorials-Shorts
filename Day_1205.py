

import spacy

nlp = spacy.load("en_core_web_sm")

nlp.Defaults.stop_words.remove("not")
nlp.vocab["not"].is_stop = False

doc = nlp('Python is not cool')

for token in doc:
    print(token.text, token.is_stop)