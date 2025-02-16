

# pip install googletrans

from googletrans import Translator


translator = Translator()
a = 'Hello, how are you'
b = translator.translate(a, dest='es').text
c = translator.translate(a, dest='fr').text
d = translator.translate(a, dest='it').text



print(f"English: {a}")
print(f"Spanish: {b}")
print(f"French: {c}")
print(f"Italian: {d}")
