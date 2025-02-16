
from dataclasses import dataclass

@dataclass
class Pet():
    name : str
    age : int

    def introduce(self):
        print(f'{self.name} is {self.age} years old')

@dataclass
class Fish(Pet):
    color : str

x = Fish(name='Bluey',color='blue',age=2)

print(f'{x.name=}, {x.age=}, {x.color=}')
x.introduce()










