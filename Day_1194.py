

class Swim():
    def swim(self):
        print("I'm swimming!")

class Run():
    def run(self):
        print("I'm running!")

class Human(Swim,Run):
    def walk(self):
        print("I'm walking!")

h = Human()
h.walk()
h.swim()
h.run()