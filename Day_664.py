

# pip install nltk

from nltk.stem import SnowballStemmer

snowball = SnowballStemmer('english')

words = ['jumping','jumped','jumps',
         'talking','talks','talked']

roots = [snowball.stem(word) for word in words]

print(roots)








