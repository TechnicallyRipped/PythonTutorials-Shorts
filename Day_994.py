

from dataclasses import dataclass,asdict

@dataclass
class Address:
    address: str
    state: str

@dataclass
class Person:
    name: str
    address: Address

p = Person('Bob', Address('101 Main Street','NY'))

print(asdict(p))
