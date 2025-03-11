

# pip install pydantic

from pydantic import BaseModel, Field

class User(BaseModel):
    username:str = Field(default='Guest',
                         min_length=3)
    age:int

x = User(age=30)
print(x)








