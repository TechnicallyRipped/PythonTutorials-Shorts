

class Dog():
    def __init__(self,name):
        self.name = name
    
    @property
    def bark(self):
        print(f'{self.name} says "Woof"')


d = Dog('Star')

d.bark











