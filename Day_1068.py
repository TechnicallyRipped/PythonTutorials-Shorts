


import random

items = ['a','b','c','d']
answer = random.choice(items)

print(f'Guess the letter from this list: {items}')

while True:
    guess = input('Current guess: ').lower()
    if guess == answer:
        print('You got it!')
        break
    else:
        print('Incorrect!')
