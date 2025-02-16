




from itertools import product as itp

letters = ['A', 'B']
numbers = [1,2]
special = ['!', '?']

combinations_list = list(itp(letters, numbers, special))

for cb in combinations_list:
    print(cb)





















