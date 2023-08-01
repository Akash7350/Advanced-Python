from faker import Faker
import json
fake=Faker()
name=[]
address=[]
location=[]
for _ in range(100):
	name.append(fake.name())
	address.append(fake.address())
	location.append(fake.location_on_land())
dt={'Name':name, 'Address':address, 'Location':location}
js=json.dumps(dt)
print("All data wing json object")
print(js)

