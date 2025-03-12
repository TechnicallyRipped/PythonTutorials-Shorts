

# pip install pydantic

from pydantic import BaseModel, Field

class Person(BaseModel):
    age:int = Field(frozen=True)

x = Person(age=20)
print(x.age)

x.age = 30
print(x.age)








