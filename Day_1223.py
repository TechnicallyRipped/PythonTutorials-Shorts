

from dataclasses import dataclass, asdict

@dataclass
class Person:
    name : str
    age : int

x = Person('Joe',35)

y = asdict(x)
print(y)
