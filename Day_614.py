


class Parent():
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):
        print("Hello from Child!")
        super().greet()

x = Child()
x.greet()








