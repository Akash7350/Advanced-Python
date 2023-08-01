from faker import Faker
fake=Faker('hi_IN')
name=[]
country=[]

for _ in range(10):
	name.append(fake.name())
	country.append(fake.country())	
print('Fake name in Hindi',name)
print('Fake contry in Hindi', country)
