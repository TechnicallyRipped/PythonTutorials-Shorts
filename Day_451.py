

from itertools import cycle

x = ['Chris','Brian','Mike']

for i,person in enumerate(cycle(x)):
    if i == 10:
        print(person)
