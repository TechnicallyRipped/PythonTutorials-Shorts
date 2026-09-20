

import spacy

nlp = spacy.load("en_core_web_sm")

nlp.Defaults.stop_words.add("python")

doc = nlp('Python is cool')

for token in doc:
    print(token.text, token.is_stop)