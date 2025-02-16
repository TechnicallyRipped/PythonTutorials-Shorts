

import random

values = ['Green', 'Blue', 'Red', 'Yellow']
weights = [0.05, 0.9, 0.025, 0.025]

random_choice = random.choices(values, weights, k=5)

print(random_choice)






















