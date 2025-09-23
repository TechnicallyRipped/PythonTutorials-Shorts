

from pydantic import BaseModel
from typing import Optional

class human(BaseModel):
    name : str
    age : Optional[int] = None
    score : int | None = None

x = human(name='Joe',age=30,score=99)

print(x)