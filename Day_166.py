



class Pet():
    def __init__(self, age):
        self.age = age
    def introduce(self):
        print(f'I am {self.age} years old')

class Dog(Pet):
    def __init__(self, age, name):
        super().__init__(age)
        self.name = name
    def bark(self):
        print(f"{self.name} say 'WOOF'")


x = Dog(10, 'Macho')

print(x.age)
print(x.name)




































