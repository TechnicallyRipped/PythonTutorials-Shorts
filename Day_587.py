

from dataclasses import dataclass

class Dog():
    def __init__(self,name,color):
        self.name = name
        self.color = color

dog1 = Dog('Sky','brown')
print(f'{dog1.name} is a {dog1.color} dog.')

@dataclass
class Dog2():
    name : str
    color : str

dog2 = Dog2('Luna','grey')
print(f'{dog2.name} is a {dog2.color} dog.')























