


class Animal():
    def __init__(self,name):
        self.name = name

    def identify(self):
        print(f"This animal's name is {self.name}")

class Dog(Animal):
    def __init__(self,name,size):
        super().__init__(name)
        self.size = size
    def size_of(self):
        print(f"The size of {self.name} is {self.size}")

d = Dog('Sky','Large')

d.identify()
d.size_of()






