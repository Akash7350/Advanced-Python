from faker import Faker
fake=Faker()
gender='M'
male_profile=fake.simple_profile(sex=gender)
print('Male profile generated: ', male_profile)

gender='F'
female_profile=fake.simple_profile(sex=gender)
print('Femal profile generated: ', female_profile)

general_profile=fake.simple_profile()
print('Femal profile generated: ', general_profile)


