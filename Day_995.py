

from dataclasses import dataclass

@dataclass(kw_only=True)
class Person():
    name: str
    age: int

p = Person(name='Mike',age=30)

print(p.name)
print(p.age)
