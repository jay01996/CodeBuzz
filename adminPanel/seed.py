from django.core.management.base import BaseCommand
from .models import Admin
from faker import Faker
import random

fake = Faker()

def generate_admins_data(n=20):
    department = ['CA','CSE','Civil','Mechanical']

    for _ in range(n):
        Admin.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
            phone_no=fake.phone_number(),
            department = random.choice(department),
            password=fake.password()
        )
    print(f"✅ Successfully created {n} fake Admins records.")

if __name__ == '__main__':
    generate_admins_data()