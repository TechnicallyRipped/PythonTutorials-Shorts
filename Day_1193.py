

class Animal():
    def talk(self):
        print(f"Unknown sound")

class Dog(Animal):
    def __init__(self):
        super().__init__()
    def talk(self):
        print("WOOF!")

a = Animal()
a.talk()

d = Dog()
d.talk()