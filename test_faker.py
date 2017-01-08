from faker import Factory

fake = Factory.create()
names = []

for _ in  range(0, 128):
    names.append(fake.first_name())

names.sort()
