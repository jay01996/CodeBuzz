from django.core.management.base import BaseCommand
from .models import Student
from faker import Faker
import random

fake = Faker()

def generate_students(n=50):
    courses = ['BCA', 'B.Tech', 'MCA', 'B.Sc', 'MBA']
    batches = ['202-2023', '2021-2024', '2022-2025']
    sessions = ['2025-26', '2026-27']
    department = ['CA','CSE','Civil','Mechanical']
    semesters = ['1', '2', '3', '4', '5', '6']
    sections = ['A', 'B', 'C', 'D','E']

    for _ in range(n):
        Student.objects.create(
            name=fake.name(),
            email=fake.unique.email(),
            phone_no=fake.phone_number(),
            batch=random.choice(batches),
            session=random.choice(sessions),
            course=random.choice(courses),
            department = random.choice(department),
            semester=random.choice(semesters),
            section=random.choice(sections),
            password=fake.password()
        )
    print(f"✅ Successfully created {n} fake student records.")

if __name__ == '__main__':
    generate_students()