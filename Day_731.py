

# pip install faker

from faker import Faker

fake = Faker('en_US')
fake.seed_instance(100)

print(fake.name())
print(fake.name())
print(fake.name())
