

import sys

class Person():
    __slots__ = ['name','age']
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # __dict__ 
x = Person("Joe",30)
x.score = 100
print(sys.getsizeof(x))







