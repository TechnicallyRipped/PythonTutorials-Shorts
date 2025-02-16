


#pip install textblob

from textblob import TextBlob

text = "I love turtles!"
blob = TextBlob(text)

polarity = blob.sentiment

print(polarity)
























