
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name:str):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

dog = Dog(name='Star')
dog.make_sound()


