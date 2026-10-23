

from dataclasses import dataclass, fields

@dataclass
class Person:
    name : str
    age : int

x = Person('Joe',35)

for f in fields(x):
    print(f.name)
