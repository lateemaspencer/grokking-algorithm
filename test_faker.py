from faker import Factory
from pprint import pprint
fake = Factory.create()
names = []

for _ in  range(0, 40):
    names.append(fake.first_name())

names.sort()
pprint(names)