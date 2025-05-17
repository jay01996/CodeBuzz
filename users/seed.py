from django.core.management.base import BaseCommand
from django.core.files import File
from users.models import Student  # Adjust import path as needed
from faker import Faker
import random
import os
from urllib.request import urlretrieve
from django.conf import settings

fake = Faker()

def download_random_profile_photo(student_id):
    # Use pravatar to get a random face
    url = f"https://i.pravatar.cc/300?u={student_id}"  # unique image per student_id
    filename = f"profile_{student_id}.jpg"
    photo_dir = os.path.join(settings.MEDIA_ROOT, 'student_photos')
    os.makedirs(photo_dir, exist_ok=True)
    local_path = os.path.join(photo_dir, filename)

    urlretrieve(url, local_path)
    return f"student_photos/{filename}"

def generate_students(n=50):
    courses = ['BCA', 'B.Tech', 'MCA', 'B.Sc', 'MBA']
    sections = ['A', 'B', 'C', 'D', 'E']
    genders = ['Male', 'Female', 'Other']
    UNIVERSITIES = ['ABC University', 'XYZ Institute', 'Tech University']
    COLLEGES = ['College of Engineering', 'School of IT', 'Business School']
    DEPARTMENTS = ['Computer Science', 'Information Technology', 'Electronics']
    BRANCHES = ['CS', 'IT', 'ECE']

    for _ in range(n):
        gender = random.choice(genders)
        full_name = fake.name_male() if gender == 'Male' else fake.name_female()
        email = fake.unique.email()

        student = Student.objects.create_user(
            email=email,
            password=fake.password(),
            full_name=full_name,
            gender=gender,
            dob=fake.date_of_birth(minimum_age=18, maximum_age=30),
            contact_number=fake.phone_number(),
            address=fake.address(),
            university=random.choice(UNIVERSITIES),
            college=random.choice(COLLEGES),
            department=random.choice(DEPARTMENTS),
            course=random.choice(courses),
            branch=random.choice(BRANCHES),
            semester=random.randint(1, 8),
            section=random.choice(sections)
        )

        # Add profile photo after saving
        photo_path = download_random_profile_photo(student.student_id)
        student.profile_photo.name = photo_path
        student.save()

    print(f"✅ Successfully created {n} fake student records.")

if __name__ == '__main__':
    generate_students()
