

# pip install nltk
# import nltk
# nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop = stopwords.words('english')
# print(stop)

text = "This is an example sentence that removes stop words."
tokenized_text = word_tokenize(text)
# print(tokenized_text)

text2 = [word for word in tokenized_text if word.lower() not in stop]
print(text2)








