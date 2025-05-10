


from textblob import TextBlob

x = 'I hav prfect speling.'

blob = TextBlob(x)

spellcheck = blob.correct()

print(spellcheck)

