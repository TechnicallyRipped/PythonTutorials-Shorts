

# pip install pydantic

from pydantic import BaseModel, Field

class Person(BaseModel):
    name:str = Field(min_length=4,
                     max_length=8)

x = Person(name='Joeeeeeeeeeee')
print(x.name)







