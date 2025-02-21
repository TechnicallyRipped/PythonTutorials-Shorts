

# pip install scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

x = ["red blue blue",
     "green blue red",
     "red red red",
     "blue green green"]

vectorizer = CountVectorizer()

vectors = vectorizer.fit_transform(x)

df = pd.DataFrame(vectors.toarray(),
                  columns=vectorizer.get_feature_names_out())

print(df)