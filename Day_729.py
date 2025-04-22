

# pip install faker

from faker import Faker

fake = Faker('en_US')

print(fake.name())
print(fake.address()) 
print(fake.email())
print(fake.date_of_birth()) 