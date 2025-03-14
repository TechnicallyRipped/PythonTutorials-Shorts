

# pip install pydantic

from pydantic import BaseModel, StrictInt,StrictFloat

class Product(BaseModel):
    quantity:StrictInt
    sale_price:StrictFloat

phone = Product(quantity=10,sale_price=499)

print(phone)




