from django.core.management.base import BaseCommand
from django.core.files import File
from accounts.models import Student, Faculty # Adjust import path as needed
from faker import Faker
import random
import os
from urllib.request import urlretrieve
from django.conf import settings
from institute.models import *

fake = Faker()

# def download_random_profile_photo(student_id):
#     # Use pravatar to get a random face
#     url = f"https://i.pravatar.cc/300?u={student_id}"  # unique image per student_id
#     filename = f"profile_{student_id}.jpg"
#     photo_dir = os.path.join(settings.MEDIA_ROOT, 'student_photos')
#     os.makedirs(photo_dir, exist_ok=True)
#     local_path = os.path.join(photo_dir, filename)

#     urlretrieve(url, local_path)
#     return f"student_photos/{filename}"

# GENDER_CHOICES = ['Male', 'Female', 'Other']

# def generate_students(n=150):
#     universities = list(University.objects.all())
#     colleges = list(College.objects.all())
#     departments = list(Department.objects.all())
#     courses = list(Course.objects.all())
#     branches = list(Branch.objects.all())
#     semesters = list(Semester.objects.all())
#     sections = list(Section.objects.all())
#     groups = list(Group.objects.all())
    
#     if not (universities and colleges and departments and courses and branches and semesters and sections and groups):
#         print("Make sure all foreign key tables have data first!")
#         return

#     for _ in range(n):
#         gender = random.choice(GENDER_CHOICES)
#         full_name = fake.name_male() if gender == 'Male' else fake.name_female()

#         student = Student(
#             university=random.choice(universities),
#             college=random.choice(colleges),
#             department=random.choice(departments),
#             course=random.choice(courses),
#             branch=random.choice(branches),
#             semester=random.choice(semesters),
#             section=random.choice(sections),
#             group=random.choice(groups),
#             full_name=full_name,
#             roll_no=fake.unique.bothify(text='ROLL####'),
#             email=fake.unique.email(),
#             password='01234',  # Ideally use hashed password for real data
#             contact_number=fake.phone_number(),
#             gender=gender,
#             dob=fake.date_of_birth(minimum_age=18, maximum_age=24),
#             address=fake.address(),
#         )

#         # Add profile photo after saving
#         photo_path = download_random_profile_photo(student.student_id)
#         student.profile_photo.name = photo_path
#         student.save()

#     print(f"✅ Successfully created {n} fake student records.")

# if __name__ == '__main__':
#     generate_students()


# fake data for the faculty table
def download_random_profile_photo(cbf_id):
    # Use pravatar to get a random face
    url = f"https://i.pravatar.cc/300?u={cbf_id}"  # unique image per cbf_id
    filename = f"profile_{cbf_id}.jpg"
    photo_dir = os.path.join(settings.MEDIA_ROOT, 'faculty_photos')
    os.makedirs(photo_dir, exist_ok=True)
    local_path = os.path.join(photo_dir, filename)

    urlretrieve(url, local_path)
    return f"faculty_photos/{filename}"

GENDER_CHOICES = ['Male', 'Female', 'Other']

def generate_faculties(n=150):
    universities = list(University.objects.all())
    colleges = list(College.objects.all())
    departments = list(Department.objects.all())

    
    if not (universities and colleges and departments):
        print("Make sure all foreign key tables have data first!")
        return

    for _ in range(n):
        gender = random.choice(GENDER_CHOICES)
        full_name = fake.name_male() if gender == 'Male' else fake.name_female()

        faculty = Faculty(
            university=random.choice(universities),
            college=random.choice(colleges),
            department=random.choice(departments),
            full_name=full_name,
            employee_id=fake.unique.bothify(text='CGC####'),
            email=fake.unique.email(),
            password='01234',  # Ideally use hashed password for real data
            contact_number=fake.phone_number(),
            gender=gender,
            dob=fake.date_of_birth(minimum_age=22, maximum_age=50),
            address=fake.address(),
        )

        # Add profile photo after saving
        photo_path = download_random_profile_photo(faculty.cbf_id)
        faculty.profile_photo.name = photo_path
        faculty.save()

    print(f"✅ Successfully created {n} fake Faculty records.")

if __name__ == '__main__':
    generate_faculties()
