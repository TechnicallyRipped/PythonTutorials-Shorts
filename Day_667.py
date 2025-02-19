

# pip install scikit-learn
from sklearn.feature_extraction.text import CountVectorizer

x = ["red blue blue",
     "green blue red"]

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(x)

print(vectors.toarray())

print(vectorizer.get_feature_names_out())

