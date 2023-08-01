import faker

fake=faker.Faker()

for _ in range(10):
	currency_name = fake.currency_name()
	currency_symbol = fake.currency_symbol()
	currency_value = fake.pyfloat()
	
for i in range(0, 10):
	print(f"Currency_Name :  {currency_name}")
	print(f"Currency_symbol : {currency_symbol}")
	print(f"Currency_value : {currency_value}")
