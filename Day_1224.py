

from dataclasses import dataclass, replace

@dataclass
class Person:
    name : str
    age : int

x = Person('Joe',35)

y = replace(x,age=50)

print(x)
print(y)