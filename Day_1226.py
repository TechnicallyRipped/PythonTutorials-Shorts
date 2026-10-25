

from dataclasses import dataclass, astuple

@dataclass
class Person:
    name : str
    age : int

x = Person('Joe',30)

y = astuple(x)

print(y)