

# pip install pydantic

from pydantic import BaseModel, Field

class Product(BaseModel):
    price: int = Field(ge=0,le=100)
# gt, ge, lt, le
phone = Product(price=50)
print(phone.price)



