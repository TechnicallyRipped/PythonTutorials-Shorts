

from word2number import w2n

x = '''one billion four hundred 
       thirty two million three 
       hundred twenty two thousand 
       nine hundred fifty one'''

num_x = w2n.word_to_num(x)

print(num_x)
print(type(num_x))




