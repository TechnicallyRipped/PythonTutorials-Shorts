

# pip install pydantic

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

x = Person(name='Joe',age=30)
print(x)



