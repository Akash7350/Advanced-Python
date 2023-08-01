from faker import Faker
import json
fake=Faker()
name=[]
address=[]
location=[]
for _ in range(10):
	name.append(fake.name())
	address.append(fake.address())
	location.append(fake.location_on_land())
	
for i in range(0, 10):
	print("Name : ", name[i])
	print("Address : ", address[i])
	print("Location : ", location[i])
	print('==========================')
