


class Person():
    def __init__(self, first:str, last:str):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

x = Person('Kim','Kardashian')

print(x.full_name)


