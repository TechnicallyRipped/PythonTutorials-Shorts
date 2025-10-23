
import sys

DEBUG = "--debug" in sys.argv
print(DEBUG)
x = 5
y = 10
z = 100

a = x + y
if DEBUG:
    print(f'a = {x} + {y} = {a}')

b = a + z

if DEBUG:
    print(f'b = {a} + {z} = {b}')

print(b)





