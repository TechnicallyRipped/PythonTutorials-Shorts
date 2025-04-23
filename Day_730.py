
# pip install faker

from faker import Faker
import pandas as pd

fake = Faker('en_US')

data = []

for i in range(10):
    data.append({'Name': fake.name(),
                 'Address': fake.address(),
                 'Email': fake.email()})

df = pd.DataFrame(data)
print(df)