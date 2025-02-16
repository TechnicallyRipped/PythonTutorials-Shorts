

# pip install num2words
from num2words import num2words

x = 121

num1 = num2words(x)
print(num1)

num2 = num2words(x,to='currency', currency='USD')
print(num2)

num3 = num2words(x, to='ordinal')
print(num3)

num4 = num2words(x, to='ordinal_num')
print(num4)










