from func import sum_numbers
from faker import Faker

sum_numbers(5,4)

print(sum_numbers(5,4))

fake = Faker("he_IL")

print(fake.name)
print(fake.address())
